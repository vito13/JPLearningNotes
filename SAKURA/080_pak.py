import genanki
import os
import random
import re

pak_name = 'SAKURA_A100'
deck_id = random.randint(1, 10**10)
model_id = random.randint(1, 10**10)

# 定义一个Anki卡片包
my_deck = genanki.Deck(
    deck_id,
    pak_name
)

# 定义Anki卡片的模板
my_model = genanki.Model(
    model_id,
    'Simple Audio and Image Model',
    fields=[
        {'name': 'Word'},
        {'name': 'Definition'},
        {'name': 'Audio'},
        {'name': 'Image'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Word}}<br>{{Audio}}',
            'afmt': '{{Audio}}{{Image}}<br><hr id="answer"><br>{{Definition}}',
        },
    ]
)

# 定义一个函数来从文件名中提取数字部分
def extract_number(file_name):
    # 使用正则表达式找到文件名中的数字部分
    match = re.search(r'\d+', file_name)
    return int(match.group()) if match else 0

# 生成示例数据
def get_demo_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取音频和图片文件夹的路径
    audio_dir = os.path.join(script_dir, 'A100/audio')
    img_dir = os.path.join(script_dir, 'A100/img')
    
    # 获取并按数字顺序排序文件名
    audio_files = sorted(os.listdir(audio_dir), key=extract_number)
    img_files = sorted(os.listdir(img_dir), key=extract_number)
    
    words = []
    for i, (audio_file, img_file) in enumerate(zip(audio_files, img_files)):
        word = f'{pak_name}_word_{i:03d}'  # 在词汇名前加上包名
        definition = f'Definition for {word}.'
        audio_file_path = os.path.join(audio_dir, audio_file)
        image_file_path = os.path.join(img_dir, img_file)
        words.append({
            'word': word,
            'definition': definition,
            'audio_file': audio_file_path,
            'image_file': image_file_path
        })
    return words

# 生成Anki卡片包
def create_anki_deck():
    word_list = get_demo_data()
    media_files = []

    for item in word_list:
        word = item['word']
        definition = item['definition']
        audio_file = item['audio_file']
        image_file = item['image_file']

        # 检查音频和图片文件是否存在
        if os.path.exists(audio_file) and os.path.exists(image_file):
            media_files.append(audio_file)
            media_files.append(image_file)
            my_note = genanki.Note(
                model=my_model,
                fields=[
                    word,
                    definition,
                    f'[sound:{os.path.basename(audio_file)}]',
                    f'<img src="{os.path.basename(image_file)}" />'
                ]
            )
            my_deck.add_note(my_note)
        else:
            if not os.path.exists(audio_file):
                print(f"音频文件不存在: {audio_file}")
            if not os.path.exists(image_file):
                print(f"图片文件不存在: {image_file}")

    # 创建Anki包
    my_package = genanki.Package(my_deck)
    my_package.media_files = media_files
    my_package.write_to_file(pak_name + ".apkg")
    print("Anki卡片包生成成功：" + pak_name + ".apkg")

if __name__ == '__main__':
    create_anki_deck()