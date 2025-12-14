from flask import Flask, request, abort
from pyngrok import ngrok
import sys

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

# LINE Bot 設定
CHANNEL_ACCESS_TOKEN = '請填入您的 Channel Access Token'
CHANNEL_SECRET = '請填入您的 Channel Secret'

# Ngrok Token
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
        print(f" * 請將此網址加上 /callback 填入 LINE Developers Console 的 Webhook URL")
        print(f" * 例如: {public_url}/callback")
    except Exception as e:
        print(f"Error connecting ngrok: {e}")
        sys.exit(1)

app = Flask(__name__)

configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    # 1. 啟動 ngrok
    start_ngrok()
    
    # 2. 啟動 Flask 應用程式
    app.run(port=5000)
