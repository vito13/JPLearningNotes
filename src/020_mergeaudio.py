ffmpeg -i "concat:011.mp3|012.mp3|013.mp3" -acodec copy output.mp3
rm 011.mp3 012.mp3 013.mp3
mv output.mp3 011.mp3