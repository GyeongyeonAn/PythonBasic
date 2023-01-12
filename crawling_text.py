# requests 자원 요청
# 200 : 요청 성공
# 404 : 페이지를 찾을 수 없음
import requests

# BeautifulSoup
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")

# 16비트의 원시 값으로 데이터 출력
print(r.content)

# html 문법으로 데이터 출력
print(r.text)

bs = BeautifulSoup(r.content, "html.parser")
print(bs)

# h3 Eliments만 출력하기
h3 = bs.select("h3")

print(h3[0].attrs)

# h3 Eliments 중 가장 첫번째를 가져오기
h3 = bs.select_one("h3")
print(h3.text)

# 자식 Eliment를 선택하여 가져오기
h3_a = bs.select_one("h3 > a")
print(h3_a)

# 클래스 이름으로 가져오기
selector = bs.select_one("div.current_box")
print(selector)

# 어떤 요소인지 상관 없이 title을 포함한 모든 class Eliments를 가져오기
selector = bs.select_one(".title")
print(selector)

selector = bs.find_all("#u_skip")
print(selector)

selector = bs.find_all("div", {"class": "partner_box"})
print(selector)

selector = bs.find("div", {"class": "partner_box"})
print(selector.text)
