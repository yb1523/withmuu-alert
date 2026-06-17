import requests

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

print("=== 위드뮤 HTML 구조 분석 테스트 ===")
response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
)

print(f"🌐 접속 상태 코드: {response.status_code} (200이면 정상 접속)")

html = response.text
target = "JOTA (조타)"
idx = html.find(target)

if idx != -1:
    print("✅ 'JOTA (조타)' 텍스트 발견 성공!")
    print("\n--- 🔍 주변 HTML 코드 구조 ---")
    # 상품명 주변의 HTML 태그들을 확인하기 위해 앞뒤 글자를 출력합니다.
    print(html[max(0, idx - 250) : idx + 50])
    print("--------------------------------")
else:
    print("❌ 'JOTA (조타)' 텍스트를 찾을 수 없습니다.")
    print("이유 1: 자바스크립트로 나중에 로딩되는 사이트일 수 있습니다.")
    print("이유 2: 사이트 내에 적힌 상품명 띄어쓰기 등이 다를 수 있습니다.")
