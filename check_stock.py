import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

print("=== 위드뮤 재고 확인 시작 ===")

# 1. 가상 브라우저 설정
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(5) # 동적 로딩 대기
html = driver.page_source
driver.quit()

# 2. HTML을 옵션(<option>) 단위로 쪼개기
options = html.split('<option')

# 검색할 타겟 (스펠링이 다를 수 있으니 핵심 영어 알파벳만 사용)
targets = ["JOTA", "MING", "ZZEROM"] 
found = []

for target in targets:
    # 쪼개진 옵션 조각들을 하나씩 검사
    for opt in options:
        # 해당 조각 안에 타겟 이름(예: JOTA)이 있다면?
        if target in opt.upper():
            # 그 조각 안에 '품절'이나 'disabled'가 "없어야만" 재고가 있는 것!
            if '품절' not in opt and 'disabled' not in opt:
                found.append(target)
            break # 찾았으면 다음 멤버로 넘어감

# 3. 결과 전송
if found:
    # 재고가 있는 멤버만 모아서 알림 전송
    msg = "🚨 위드뮤 재입고 발견!\n\n" + "\n".join(found)
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": msg}
    )
    print(f"✅ 재고 발견! 텔레그램 알림 전송 완료: {found}")
else:
    print("❌ 아직 재고가 풀리지 않았습니다. (전원 품절 상태)")
