import os

# 指定要重命名的文件夹路径
folder_path = '/home/rockylinux/projects/JPLearningNotes/res/audio'

# 切换到指定的文件夹
os.chdir(folder_path)

# 获取文件夹中的所有文件
files = os.listdir()
# 按文件修改时间排序
files.sort(key=lambda x: os.path.getmtime(x))

# 批量重命名文件
for index, filename in enumerate(files):
    # 分离文件名和扩展名
    file_name, file_extension = os.path.splitext(filename)
    # 创建新的文件名，格式为三位数字
    new_filename = f'{index:03d}{file_extension}'  # 示例：将文件名修改为 000.txt, 001.jpg 等
    os.rename(filename, new_filename)


print("audio文件重命名完成！")

# 指定要重命名的文件夹路径
folder_path = '/home/rockylinux/projects/JPLearningNotes/res/img'

# 切换到指定的文件夹
os.chdir(folder_path)

# 获取文件夹中的所有文件
files = os.listdir()
# 按文件修改时间排序
files.sort(key=lambda x: os.path.getmtime(x))

# 批量重命名文件
for index, filename in enumerate(files):
    # 分离文件名和扩展名
    file_name, file_extension = os.path.splitext(filename)
    # 创建新的文件名，格式为三位数字
    new_filename = f'{index:03d}{file_extension}'  # 示例：将文件名修改为 000.txt, 001.jpg 等
    os.rename(filename, new_filename)


print("img文件重命名完成！")
