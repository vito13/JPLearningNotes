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
    |找词库|  待开始  | 
    |找例句|  待开始  | 
    |找图片|   待开始 | 
    |中日英翻译|  待开始  | 
    |中日英音频| 待开始   | 
    |打包| 待开始 | 
    |发布| 待开始 | 

 


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