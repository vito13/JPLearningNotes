#!/bin/bash

# 定义音频目录
audio_dir="./audio"

# 进入音频目录
cd "$audio_dir" || exit

# 定义需要合并的音频文件组
audio_pairs=(
    "1_191.mp3 1_192.mp3"
    "1_218.mp3 1_219.mp3"
    "1_346.mp3 1_347.mp3"
    "1_350.mp3 1_351.mp3"
)

# 循环遍历每一组音频文件并合并
for pair in "${audio_pairs[@]}"; do
    # 将每组的两个音频文件拆分开
    read -r file1 file2 <<< "$pair"
    
    # 合并音频并自动覆盖 file1
    ffmpeg -y -i "concat:$file1|$file2" -acodec copy "$file1"
    
    # 移动第二个音频文件
    mv "$file2" ../
done
