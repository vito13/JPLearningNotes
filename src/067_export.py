import zipfile
import sqlite3
import os
import csv
import json

def extract_apkg(apkg_path, extract_to):
    with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def parse_anki_db(db_path, media_json_path, media_dir, output_csv, updated_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 加载媒体文件映射
    with open(media_json_path, 'r', encoding='utf-8') as f:
        media_mapping = json.load(f)

    # 获取模型定义
    cursor.execute("SELECT models FROM col")
    models_data = cursor.fetchone()[0]
    models = json.loads(models_data)

    # 创建一个模型 ID 到字段名称的映射
    model_field_map = {}
    for model_id, model_info in models.items():
        field_names = [field["name"] for field in model_info["flds"]]
        model_field_map[model_id] = field_names

    # 查询所有笔记
    cursor.execute("SELECT guid, flds, sfld, mid FROM notes")
    rows = cursor.fetchall()

    # 获取所有可能的字段名称集合
    all_fieldnames = set()
    for row in rows:
        mid = row[3]
        field_names = model_field_map.get(str(mid), [])
        all_fieldnames.update(field_names)

    # 添加额外的字段名称
    all_fieldnames = ['guid', 'Primary Field'] + list(all_fieldnames)

    # 生成 CSV 文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_fieldnames)
        writer.writeheader()

        for row in rows:
            guid, flds, sfld, mid = row
            fields = flds.split('\x1f')  # Anki 用特殊字符分隔字段

            # 根据模型 ID 获取字段名称
            field_names = model_field_map.get(str(mid), [])

            # 创建一个记录字典
            record = {'guid': guid, 'Primary Field': sfld}
            for i, field_value in enumerate(fields):
                if i < len(field_names):
                    field_name = field_names[i]
                    record[field_name] = field_value

            # 将记录写入 CSV
            writer.writerow(record)

    # 处理媒体文件映射并更新 CSV 文件
    update_csv_with_media(media_mapping, output_csv, updated_csv)

    cursor.close()
    conn.close()

def update_csv_with_media(media_mapping, output_csv, updated_csv):
    # 创建文件名到索引的映射
    value_to_key_mapping = {v: k for k, v in media_mapping.items()}

    rows = []
    with open(output_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        for row in reader:
            # 替换图片字段
            if 'Image_URI' in row and row['Image_URI']:
                image_tag = row['Image_URI']
                if 'src="' in image_tag:
                    start = image_tag.index('src="') + len('src="')
                    end = image_tag.index('"', start)
                    image_filename = image_tag[start:end]
                    if image_filename in value_to_key_mapping:
                        new_image_filename = value_to_key_mapping[image_filename]
                        row['Image_URI'] = f'<img src="{new_image_filename}" />'

            # 替换音频字段
            audio_fields = ['Audio', 'Audio']
            for field in audio_fields:
                if field in row and row[field]:
                    audio_tag = row[field]
                    if 'sound:' in audio_tag:
                        start = audio_tag.index('sound:') + len('sound:')
                        end = audio_tag.index(']', start)
                        audio_filename = audio_tag[start:end]
                        if audio_filename in value_to_key_mapping:
                            new_audio_filename = value_to_key_mapping[audio_filename]
                            row[field] = f'[sound:{new_audio_filename}]'

            rows.append(row)

    # 写入修改后的 CSV 文件，确保正确处理字段中的特殊字符
    with open(updated_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    # 加载配置文件
    config = load_config('/home/rockylinux/projects/JPLearningNotes/src/apkg.json')
    apkg_files = config['apkg_files']
    output_base = config['output_directory']  # 获取输出根目录

    for apkg_path in apkg_files:
        # 确保Anki包路径存在
        if not os.path.isfile(apkg_path):
            print(f"Anki包文件 {apkg_path} 不存在，跳过...")
            continue

        # 获取Anki包文件的目录和名称
        base_dir = os.path.dirname(apkg_path)
        filename = os.path.splitext(os.path.basename(apkg_path))[0]
        extract_to = os.path.join(output_base, f"{filename}_export")  # 使用指定的输出根目录

        # 创建解压目录
        os.makedirs(extract_to, exist_ok=True)

        # 输出CSV路径
        output_csv = os.path.join(extract_to, f"{filename}_output.csv")
        updated_csv = os.path.join(extract_to, f"{filename}_updated_output.csv")

        # 步骤 1: 解压 .apkg 文件
        extract_apkg(apkg_path, extract_to)

        # 数据库路径和媒体文件路径
        db_path = os.path.join(extract_to, 'collection.anki21')
        media_json_path = os.path.join(extract_to, 'media')

        # 步骤 2: 解析数据库并更新 CSV
        parse_anki_db(db_path, media_json_path, extract_to, output_csv, updated_csv)
        print(f"Anki包 {apkg_path} 解析成功，生成CSV文件：{updated_csv}")

if __name__ == '__main__':
    main()
