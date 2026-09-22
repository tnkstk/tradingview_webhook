from fastapi import FastAPI, Request
from linebot import LineBotApi
from linebot.models import TextSendMessage

app = FastAPI()

LINE_CHANNEL_ACCESS_TOKEN = "GVZcdcjpnholNWhXxX+kW2gRW1WJDZP1JRGzG7d+AOcK1VZQ1Vh858UU1lJt0k46bIpckesiYoveLl+ONdxvYs82ab4E9eDeqJNRmDuhEkTbKqMDX6CmRp+BqIwa++2+hJaRsBD+wTVV0kFPTKIfGgdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

USER_ID = "Ua31e32a6930912c89a81dcd797c8724d"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Received:", data)

    message = f"TradingView Alert:\n{data}"
    line_bot_api.push_message(USER_ID, TextSendMessage(text=message))

    return {"status": "ok"}

