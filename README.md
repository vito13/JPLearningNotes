# JPLearningNotes

## desc

## 开发列表

- vm选用virualbox
- OS选用rockylinux-8
    ```
    https://www.linuxvmimages.com/images/rockylinux-8/
    Username: rockylinux
    Password : rockylinux
    (to become root, use sudo su -)
    ```
- 语言python

## log

### 20240901

- 创建项目，用于记录日语学习的笔记，便于后期整理对知识进行总结
- note里放的都是笔记，src用于后期的代码
- 已经将n5的文法笔记进行了表格整理并提交

### 20241007

- 最近在使用anki，发现这是个好东西，下载了几个包用于背单词，但是有些内容不是太理想，想要自己去完善一下包内容，故产生了下面的计划
- 目标：用于背单词，包含如下内容：

    ```
    日语单词读音  
    日语单词的英文释义文本  
    单词配图  
    日语例句读音  
    furigana 带有假名与汉字的日语单词文本  
    furigana 日语例句内容文本  
    日语例句的英文释义文本  
    ```
- 有几个技术点需要先解决，貌似没一样都挺难。。。开干，每天干一点

    |要做的事情|子项目|当前的状态|
    |-|-|-|
    |搭建开发环境||     
    ||安装linux虚拟机|✔️|
    ||设置vscode remote ssh|✔️|
    ||安装python环境|✔️|
    |初步设计||
    ||数据库设计|进行中|
    |找词库||  待开始 |
    |找例句||  待开始 |
    |找图片||   待开始|
    |中日英翻译||  待开始 |
    |中日英音频|| 待开始  |
    |开发|||
    ||测试py库生成anki包|✔️|
    ||可以生成包含图片的anki包|✔️|
    ||可以生成包含音频的anki包|✔️|
    ||解析anki包的音频|✔️|
    ||解析anki包的图片|✔️|
    ||解析anki包的数据结构|✔️|
    ||创建包含卡片内容数据库|待开始|
    ||添加导入方式|待开始|
    |发布|| 待开始|

 


### 20241008

- 装linux，设置ssh，防火墙
    ```
    sudo dnf install -y openssh-server
    sudo systemctl start sshd
    sudo systemctl enable sshd
    sudo systemctl status sshd
    sudo firewall-cmd --permanent --add-service=ssh
    sudo firewall-cmd --reload
    
    ```

### 20241009

- 为虚拟机添加第二块网卡用于host连接，并记入ip，暂未设为静态
- 修改linux的root密码
    ```
    sudo su -
    passwd
    ip addr

    /etc/ssh/sshd_config 此文件里默认下面两个是如此
    PermitRootLogin yes
    PasswordAuthentication yes
    ```
- 使用vscode建立ssh连入
- 待在linux上修改权限设置，不要使用root进行ssh

### 20241011

- 设置用户拥有root权限

    ```
    使用root修改/etc/sudoers文件，在root那行下面添加一行，进行添加权限
    root    ALL=(ALL)       ALL
    rockylinux    ALL=(ALL)       NOPASSWD:ALL

    换回rockylinux，执行下面会打印出“root”与“所有账号密码”
    sudo whoami 
    sudo cat /etc/shadow
    ```

- 使用win的vscode创建ssh连接，使用rockylinux用户
- 创建/home/rockylinux/projects目录作为开发根目录，并用vscode进行开启
- 安装git

    ```
    sudo dnf install git
    git --version
    git config --global user.name "。。。。。。"
    git config --global user.email "。。。。。。"
    git config --list
    git clone https://github.com/vito13/JPLearningNotes.git
    ```

### 20241012

- vscode安装python扩展
- 在终端里执行如下
    ```
        [rockylinux@rocky8 JPLearningNotes]$ python3 --version
        Python 3.6.8
        [rockylinux@rocky8 JPLearningNotes]$ python3 -m pip --version
        pip 9.0.3 from /usr/lib/python3.6/site-packages (python 3.6)
        
        [rockylinux@rocky8 JPLearningNotes]$ sudo python3 -m pip install virtualenv
        [rockylinux@rocky8 JPLearningNotes]$ sudo python3 -m pip install --upgrade pip
        
        创建虚拟环境
        [rockylinux@rocky8 JPLearningNotes]$ python3 -m venv venv
        使用虚拟环境
        [rockylinux@rocky8 JPLearningNotes]$ source venv/bin/activate
        可以使用 deactivate 退出, 使用 rm -rf venv 删除虚拟环境
        
        (venv) [rockylinux@rocky8 JPLearningNotes]$ pip freeze > requirements.txt
        (venv) [rockylinux@rocky8 JPLearningNotes]$ pip install black
    ```
- 重启vscode，在command里选择Python: Select Interpreter，再选择带有venv的虚拟环境里的解释器
- vscode左下角齿轮、settings、Python Formatting Provider、选择black
- 在项目根目录创建src、test目录、和文件.gitignore，并将下面的内容放里面
    ```
    venv/
    __pycache__/
    *.pyc
    .DS_Store
    .vscode/
    ```
- 根目录建立文件.env，写入SECRET_KEY=xxx，保存，执行下面
    ```
    (venv) [rockylinux@rocky8 JPLearningNotes]$ pip install python-dotenv
    ```
- src内建立t.py，插入如下
    ```
    from dotenv import load_dotenv
    import os

    load_dotenv()
    secret_key = os.getenv("SECRET_KEY")
    print(secret_key)  # 打印 secret_key，检查是否加载成功
    ```
- 运行测试
    ```
    (venv) [rockylinux@rocky8 JPLearningNotes]$ python src/t.py 
    xxx
    ```

### 20241013

- vscode添加ssh免密
    ```
    执行 C:\Users\Administrator>ssh-keygen
    将C:\Users\Administrator\.ssh\id_rsa.pub 拷贝到 /home/rockylinux/.ssh/
    [rockylinux@rocky8 .ssh]$ cat id_rsa.pub >> authorized_keys
    在 C:\Users\Administrator\.ssh\config 文件追加一行  IdentityFile "C:\Users\Administrator\.ssh\id_rsa"
    ```
- 数据库初步设计
    
    |字段|说明|类型|
    |-|-|-|
    |単語||
    ||日本語の読み方|audio|
    ||ふりがな|text|
    ||英語|可选text|
    ||中国語|可选text|
    |配图||image|
    |例句||
    ||ふりがな|text|
    ||読み方|audio|
    ||英語|可选text|
    ||中国語|可选text|
    |笔记||image、text|
    |level|N12345|number|
    |词性|名动形副量|text|
    |类别|食物、动物、家电。。。|text|

- 待进行表设计

### 20241014

- 添加库用于测试生成apkg包

    ```
    pip install genanki
    pip install pandas
    ```

- 测试仅最简包封装，包含2个字段，一条数据

    ```
    import genanki

    # 定义一个模型（即卡片的模板）
    my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Question}}',  # 这部分定义卡片的前面
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # 这部分定义卡片的后面
        },
    ])

    # 创建一个卡包（相当于一个牌组）
    my_deck = genanki.Deck(
    2059400110,
    'Sample Deck')

    # 添加卡片
    my_note = genanki.Note(
    model=my_model,
    fields=['What is the capital of France?', 'Paris'])
    my_deck.add_note(my_note)

    # 保存卡包到文件
    genanki.Package(my_deck).write_to_file('output.apkg')

    ```

### 20241015

- 测试完成向包里加入图片的代码，pc端可见，但平板上依然见不到，待检查
    ```
    图片路径/home/rockylinux/projects/JPLearningNotes/res/img/456.jpg
    代码/home/rockylinux/projects/JPLearningNotes/test/03_zip.py

    import genanki

    my_model = genanki.Model(
    1380120064,
    'Example',
    fields=[
        {'name': 'Object'},
        {'name': 'Image'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Object}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Image}}',
        },
    ])

    my_note = genanki.Note(
    model=my_model,
    fields=['JPEG File', '<img src="456.jpg" />'])

    my_deck = genanki.Deck(
    2059400191,
    'Example')

    my_deck.add_note(my_note)

    my_package = genanki.Package(my_deck)
    my_package.media_files = ['res/img']

    my_package.write_to_file('456456.apkg')
    ```

### 20241016

- 完成可以加入图片与音频的简单demo
    
    ```
    import genanki
    import os

    # 定义一个Anki卡片包
    my_deck = genanki.Deck(
        1234567890,
        'Demo Deck with Local Audio and Images')

    # 定义Anki卡片的模板
    my_model = genanki.Model(
        987654321,
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
                'qfmt': '{{Word}}<br>{{Audio}}<br>{{Image}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Definition}}',
            },
        ])

    # 生成示例数据
    def get_demo_data():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 一个简单的词汇表
        words = [
            {
                'word': 'apple',
                'definition': 'A fruit that is typically red, green, or yellow.',
                'audio_file': os.path.join(script_dir, '..', 'res', 'audio', '123.mp3'),
                'image_file': os.path.join(script_dir, '..', 'res', 'img', '456.jpg')
            },
            {
                'word': 'banana',
                'definition': 'A long curved fruit which grows in clusters and has soft pulpy flesh.',
                'audio_file': os.path.join(script_dir, '..', 'res', 'audio', '123.mp3'),
                'image_file': os.path.join(script_dir, '..', 'res', 'img', '456.jpg')
            },
        ]
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
        my_package.write_to_file("demo_with_local_audio_and_images.apkg")
        print("Anki卡片包生成成功：demo_with_local_audio_and_images.apkg")

    if __name__ == '__main__':
        create_anki_deck()
    ```

- 使用anki导出时候勾选支持较久的版本
- 完成可以解析出anki的图片音频与卡片信息，但由于同一包内卡片排列顺序不一致，导致分割结不同，待完善此处
- 另外不同模板的卡片字段数量也不一致，此处需要注意

### 20241017

- 对anki包进行解析初步完毕

    ```
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
        # 创建一个值到键的映射，因为我们要用 CSV 中的长名称查找简短文件名
        value_to_key_mapping = {v: k for k, v in media_mapping.items()}
        # 读取 CSV 文件并更新图片和音频字段
        with open(output_csv, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            rows = []
            for row in reader:
                # 替换图片字段
                if 'Sentence-Image' in row and row['Sentence-Image']:
                    image_tag = row['Sentence-Image']
                    # 提取图片文件名
                    if 'src="' in image_tag:
                        start = image_tag.index('src="') + len('src="')
                        end = image_tag.index('"', start)
                        image_filename = image_tag[start:end]
                        if image_filename in value_to_key_mapping:
                            new_image_filename = value_to_key_mapping[image_filename]
                            # 用新的文件名替换原有的
                            row['Sentence-Image'] = f'<img src="{new_image_filename}" />'
                # 替换音频字段
                audio_fields = ['Vocabulary-Audio', 'Sentence-Audio']
                for field in audio_fields:
                    if field in row and row[field]:
                        audio_tag = row[field]
                        # 提取音频文件名
                        if 'sound:' in audio_tag:
                            start = audio_tag.index('sound:') + len('sound:')
                            end = audio_tag.index(']', start)
                            audio_filename = audio_tag[start:end]
                            if audio_filename in value_to_key_mapping:
                                new_audio_filename = value_to_key_mapping[audio_filename]
                                # 用新的文件名替换原有的
                                row[field] = f'[sound:{new_audio_filename}]'
                rows.append(row)
        # 写入修改后的 CSV 文件，确保正确处理字段中的特殊字符
        with open(updated_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        cursor.close()
        conn.close()
    def main():
        apkg_path = '/home/rockylinux/projects/JPLearningNotes/test/0105.apkg'  # 修改为你的 Anki 包路径
        extract_to = '/home/rockylinux/projects/JPLearningNotes/test/export'  # 解压文件的目标目录
        output_csv = 'output.csv'  # 原始 CSV 输出文件
        updated_csv = 'updated_output.csv'  # 修改后的 CSV 输出文件
        # 步骤 1: 解压 .apkg 文件
        extract_apkg(apkg_path, extract_to)
        # 文件路径
        db_path = os.path.join(extract_to, 'collection.anki21')
        media_json_path = os.path.join(extract_to, 'media')
        media_dir = extract_to
        # 步骤 2: 解析数据库并更新 CSV
        parse_anki_db(db_path, media_json_path, media_dir, output_csv, updated_csv)
        print(f"更新后的 CSV 文件生成成功：{updated_csv}")
    if __name__ == '__main__':
        main()
    ```