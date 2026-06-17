import requests

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

BOT_TOKEN = "BOT_TOKEN"
CHAT_ID = "CHAT_ID"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

alerts = []

if 'JOTA (조타)</option>' in html and 'disabled="disabled"' not in html.split('JOTA (조타)')[0][-300:]:
    alerts.append("JOTA")

if 'MING (밍)</option>' in html and 'disabled="disabled"' not in html.split('MING (밍)')[0][-300:]:
    alerts.append("MING")

if 'ZZEROMMING (제로밍)</option>' in html and 'disabled="disabled"' not in html.split('ZZEROMMING (제로밍)')[0][-300:]:
    alerts.append("ZZEROMMING")

if alerts:
    msg = "🚨 위드뮤 재입고 발견!\n\n" + "\n".join(alerts)

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )
