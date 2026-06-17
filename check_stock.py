import requests

URL = "https://withmuu.com/goods/goods_view.php?goodsNo=1000014598"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
)
response.encoding = 'utf-8'  # 한글 깨짐 방지
html = response.text

print("=== 3차: 도대체 뭘 읽어온 걸까? ===")
title_start = html.find("<title>")
title_end = html.find("</title>")

if title_start != -1 and title_end != -1:
    print("📄 페이지 제목:", html[title_start + 7 : title_end])
else:
    print("📄 페이지 제목: 찾을 수 없음")

print("\n--- 🔍 HTML 앞부분 500글자 훔쳐보기 ---")
print(html[:500])
