import os
import requests

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

targets = [
    "JOTA (조타)",
    "MING (밍)",
    "ZZEROMMING (제로밍)"
]

found = []

for target in targets:
    idx = html.find(target)

    if idx != -1:
        chunk = html[max(0, idx - 300):idx]

        if 'disabled="disabled"' not in chunk:
            found.append(target)

if found:
    msg = "🚨 위드뮤 재입고 발견!\n\n" + "\n".join(found)

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )
