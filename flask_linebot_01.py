from flask import (
    Flask,
    request,
    abort,
    render_template
    )

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import ( # 傳訊息
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage # 傳輸回Line官方後台的資料格式
)
from linebot.v3.webhooks import (
    MessageEvent, # 單純傳訊息 # 傳輸過來方法
    TextMessageContent # 因特定事件傳訊息 例:退群訊息 # 使用者傳過來的資料格式
)

from handle_keys import get_secret_and_token
keys = get_secret_and_token()
app = Flask(__name__) # Flask
handler = WebhookHandler(keys['channel_secret_key'])
configuration = Configuration(access_token=keys['channel_access_token'])


@app.route('/')
def say_hello_world(username=''):
    return render_template('hello.html',name=username)
    # 設計一個 #callback 的路由, 提供給 Line 官方後台去呼叫
    # 也就是所謂的呼叫 Webhook Server
    # 因為官方會把使用者傳輸的訊息轉傳給 Webhook Server
    # 所以會使用 RESTful API 的 POST 方法
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature'] # 標頭檔

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

    # 根據不同的使用者事件(event),去用不同的方式回應
    # eg. MessageEvent 代表使用者單純傳訊息的事件
    # TextMessageContent 代表使用者傳輸的訊息內容是文字
    # 符合兩個條件的事件,會被handle_message 所處理
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)] # 改詞
            )
        )

if __name__ == "__main__":
    app.run(debug=True)