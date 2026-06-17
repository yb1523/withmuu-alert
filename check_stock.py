import requests

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
).text

print("=== 2차 정밀 탐색 테스트 ===")

if "조타" in html:
    idx = html.find("조타")
    print("✅ '조타' 단어 발견! (띄어쓰기 문제였음)")
    print("--- 주변 코드 ---")
    print(html[max(0, idx - 150):idx + 150])
elif "JOTA" in html:
    idx = html.find("JOTA")
    print("✅ 'JOTA' 단어 발견! (띄어쓰기 문제였음)")
    print("--- 주변 코드 ---")
    print(html[max(0, idx - 150):idx + 150])
else:
    print("❌ '조타', 'JOTA' 둘 다 HTML 뼈대에 없습니다.")
    print("👉 결론: 이 사이트는 자바스크립트로 옵션을 숨겨놓는 쇼핑몰입니다. 전략을 바꿔야 합니다!")
