from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
print(secret_key)  # 打印 secret_key，检查是否加载成功
