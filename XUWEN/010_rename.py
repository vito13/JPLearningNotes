# import os

# def rename_files_in_directory(directory):
#     # 切换到指定的文件夹
#     os.chdir(directory)

#     # 获取文件夹中的所有文件
#     files = os.listdir()
#     # 按文件名的字母顺序排序
#     files.sort()

#     # 批量重命名文件
#     for index, filename in enumerate(files):
#         # 确保只重命名文件，忽略子文件夹
#         if os.path.isfile(filename):
#             # 分离文件名和扩展名
#             file_name, file_extension = os.path.splitext(filename)
#             # 创建新的文件名，格式为三位数字
#             new_filename = f'{index:03d}{file_extension}'  # 示例：将文件名修改为 000.txt, 001.jpg 等
#             os.rename(filename, new_filename)
#             print(f'Renamed: {filename} -> {new_filename}')

# if __name__ == "__main__":
#     # 以你刚才创建的目录为根目录，例如：
#     root_directory = '/home/rockylinux/projects/JPLearningNotes/XUWEN/life100_1'
    
#     # 组合出 img 和 audio 的路径
#     img_dir = os.path.join(os.getcwd(), root_directory, 'img')
#     audio_dir = os.path.join(os.getcwd(), root_directory, 'audio')

#     # 检查是否存在 img 和 audio 目录并进行重命名
#     if os.path.exists(img_dir):
#         print(f"Renaming files in {img_dir}...")
#         rename_files_in_directory(img_dir)

#     if os.path.exists(audio_dir):
#         print(f"Renaming files in {audio_dir}...")
#         rename_files_in_directory(audio_dir)


import os
import json
import re

CONFIG_FILE = 'config.json'  # 配置文件名

def natural_sort_key(s):
    """定义自然排序的关键函数"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def rename_files_in_directory(directory):
    # 切换到指定的文件夹
    os.chdir(directory)

    # 获取文件夹中的所有文件
    files = os.listdir()
    # 按文件名的字母顺序排序
    files = sorted(files, key=natural_sort_key)

    # 批量重命名文件
    for index, filename in enumerate(files):
        # 确保只重命名文件，忽略子文件夹
        if os.path.isfile(filename):
            # 分离文件名和扩展名
            file_name, file_extension = os.path.splitext(filename)
            # 创建新的文件名，格式为三位数字
            new_filename = f'{index:03d}{file_extension}'  # 示例：将文件名修改为 000.txt, 001.jpg 等
            os.rename(filename, new_filename)
            print(f'Renamed: {filename} -> {new_filename}')

def load_paths_from_config():
    # 读取配置文件中的路径
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            config_data = json.load(config_file)
        return config_data
    else:
        print(f"No config file found: {CONFIG_FILE}")
        return None

if __name__ == "__main__":
    # 从配置文件中读取路径
    config_data = load_paths_from_config()

    if config_data:
        img_dir = config_data['img_dir']
        audio_dir = config_data['audio_dir']

        # 检查是否存在 img 和 audio 目录并进行重命名
        if os.path.exists(img_dir):
            print(f"Renaming files in {img_dir}...")
            rename_files_in_directory(img_dir)

        if os.path.exists(audio_dir):
            print(f"Renaming files in {audio_dir}...")
            rename_files_in_directory(audio_dir)
