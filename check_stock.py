import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

print("=== 위드뮤 재고 확인 시작 ===")

# 1. 가상 크롬 브라우저 설정
chrome_options = Options()
chrome_options.add_argument('--headless') # 화면을 띄우지 않고 몰래 실행
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(options=chrome_options)

print("🌐 사이트 접속 중...")
driver.get(URL)

# 2. 쇼핑몰 옵션이 나타날 때까지 5초 대기
time.sleep(5) 

# 3. 브라우저가 본 전체 화면 HTML 가져오기
html = driver.page_source
driver.quit()

print("✅ 화면 읽기 완료! 재고 분석 시작...")

# 4. 재고 파악 로직
targets = [
    "JOTA (조타)",
    "MING (밍)",
    "ZZEROMMING (제로밍)"
]

found = []

for target in targets:
    idx = html.find(target)
    
    if idx != -1:
        # 단어를 찾았다면 그 앞뒤 글자들을 떼어와서 '품절' 관련 단어가 있는지 확인
        chunk = html[max(0, idx - 200):idx + 100]
        
        # 쇼핑몰들이 흔히 쓰는 품절 표시 방식들
        if 'disabled' not in chunk and 'sold' not in chunk.lower() and '품절' not in chunk:
            found.append(target)
    else:
        print(f"⚠️ 경고: 화면에서 '{target}' 자체를 찾지 못했습니다.")

if found:
    msg = "🚨 위드뮤 재입고 발견!\n\n" + "\n".join(found)
    
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )
    print("📲 텔레그램 알림 전송 완료!")
else:
    print("❌ 아직 재고가 풀리지 않았습니다.")
