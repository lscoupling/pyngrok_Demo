from flask import Flask
from pyngrok import ngrok
import sys

# 定義 ngrok token
# 注意：在真實專案中，建議將敏感資訊放在環境變數中，不要直接寫在程式碼裡
NGROK_TOKEN = '請填入您的 Ngrok Auth Token'

def start_ngrok():
    """設定並啟動 ngrok tunnel"""
    # 設定 token
    ngrok.set_auth_token(NGROK_TOKEN)
    
    # 建立連線到 port 5000
    # bind_tls=True 代表使用 HTTPS
    try:
        public_url = ngrok.connect(5000, bind_tls=True).public_url
        print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")
    except Exception as e:
        print(f"Error connecting ngrok: {e}")
        sys.exit(1)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/<name>")
def hello(name):
    return f"Hello {name}"

if __name__ == '__main__':
    # 1. 啟動 ngrok
    start_ngrok()
    
    # 列出所有路由規則，方便查看
    print("\n=== 目前的路由規則 (Routes) ===")
    print(app.url_map)
    print("===============================\n")

    # 2. 啟動 Flask 應用程式
    # 在 Codespaces 中通常不需要 host='0.0.0.0' 如果你是用 ngrok，
    # 因為 ngrok 會轉發本地的 localhost:5000
    app.run(port=5000)
