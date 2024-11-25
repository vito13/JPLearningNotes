# import os

# def create_subdirectories(name):
#     # 在当前目录下创建指定名称的子目录
#     base_dir = os.path.join(os.getcwd(), name)
#     os.makedirs(base_dir, exist_ok=True)

#     # 在子目录下创建 img 和 audio 子目录
#     img_dir = os.path.join(base_dir, 'img')
#     audio_dir = os.path.join(base_dir, 'audio')
    
#     os.makedirs(img_dir, exist_ok=True)
#     os.makedirs(audio_dir, exist_ok=True)

#     print(f"Created directories: {img_dir}, {audio_dir}")

# if __name__ == "__main__":
#     name = input("Enter directory name: ")
#     create_subdirectories(name)


import os
import json

CONFIG_FILE = 'config.json'  # 配置文件名

def create_subdirectories(name):
    # 在当前目录下创建指定名称的子目录
    base_dir = os.path.join(os.getcwd(), name)
    os.makedirs(base_dir, exist_ok=True)

    # 在子目录下创建 img 和 audio 子目录
    img_dir = os.path.join(base_dir, 'img')
    audio_dir = os.path.join(base_dir, 'audio')
    
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    # 将路径保存到配置文件
    config_data = {
        'base_dir': base_dir,
        'img_dir': img_dir,
        'audio_dir': audio_dir
    }
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config_data, config_file)

    print(f"Created directories: {img_dir}, {audio_dir}")
    print(f"Paths saved to {CONFIG_FILE}")

if __name__ == "__main__":
    name = input("Enter directory name: ")
    create_subdirectories(name)
