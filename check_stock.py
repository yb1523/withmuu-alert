import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

# 가상 브라우저 띄우기
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(5) # 옵션 뜰 때까지 5초 대기
html = driver.page_source
driver.quit()

print("=== 위드뮤 옵션 HTML 정밀 분석 ===")

# 1. 품절 표시 방식 확인하기
idx_jota = html.find("조타")
if idx_jota != -1:
    print("\n[🔍 조타 주변 HTML]")
    print(html[max(0, idx_jota - 200) : idx_jota + 100])
else:
    print("❌ 조타를 찾을 수 없습니다.")

# 2. 제로밍의 정확한 영어 스펠링/띄어쓰기 확인하기
idx_zero = html.find("제로밍")
if idx_zero != -1:
    print("\n[🔍 제로밍 주변 HTML]")
    print(html[max(0, idx_zero - 100) : idx_zero + 100])
else:
    print("❌ 제로밍을 찾을 수 없습니다.")
