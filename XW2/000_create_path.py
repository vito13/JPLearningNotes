import os
import json

CONFIG_FILE = 'config.json'  # 配置文件名

def create_subdirectories(name):
    # 在当前目录下创建指定名称的主目录
    base_dir = os.path.join(os.getcwd(), name)
    os.makedirs(base_dir, exist_ok=True)

    # 定义子目录
    directories = {
        'sentence_img_dir': os.path.join(base_dir, 'sentence_img'),
        'sentence_audio_dir': os.path.join(base_dir, 'sentence_audio'),
        'word_img_dir': os.path.join(base_dir, 'word_img'),
        'word_audio_dir': os.path.join(base_dir, 'word_audio')
    }

    # 创建子目录
    for key, path in directories.items():
        os.makedirs(path, exist_ok=True)

    # 将路径保存到配置文件
    config_data = {'base_dir': base_dir, **directories}
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    # 打印成功信息
    print(f"Created directories:")
    for key, path in directories.items():
        print(f"  - {key}: {path}")
    print(f"Paths saved to {CONFIG_FILE}")

if __name__ == "__main__":
    name = input("Enter directory name: ")
    create_subdirectories(name)
