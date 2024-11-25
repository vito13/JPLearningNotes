#!/bin/bash

# https://www.bearaudiotool.com/zh/


# 定义音频目录
audio_dir="./audio2"

# 进入音频目录
cd "$audio_dir" || exit

# 定义需要合并的音频文件组
audio_pairs=(
    "2_051.mp3 2_052.mp3"
    "2_055.mp3 2_056.mp3"
    "2_067.mp3 2_068.mp3"
    "2_071.mp3 2_072.mp3"
    "2_081.mp3 2_082.mp3"
    "2_112.mp3 2_113.mp3"
    "2_126.mp3 2_127.mp3"
    "2_143.mp3 2_144.mp3"
    "2_202.mp3 2_203.mp3"
    "2_216.mp3 2_217.mp3"
    "2_236.mp3 2_237.mp3"
    "2_281.mp3 2_282.mp3"
    "2_306.mp3 2_307.mp3"
    "2_346.mp3 2_347.mp3"
    "2_365.mp3 2_366.mp3"
    "2_371.mp3 2_372.mp3"
    "2_375.mp3 2_376.mp3"
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
