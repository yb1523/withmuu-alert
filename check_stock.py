import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": "✅ GitHub Actions 테스트 성공"
    }
)

print("test sent")
