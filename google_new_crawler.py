# 웹페이지에 들어가지 않고
# 뉴스 검색, 기사 제목, 링크, 게시 날짜를 엑셀에 담아서 출력
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹페이지에 들어가지 않고 검색

keyword = input("검색하고자 하는 키워드를 입력해주세요. > ")

r = requests.get(
    "https://news.google.com/search?q="+keyword+"&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

# 기사 제목, 링크
# titles = bs.select("div.xrnccd > article > h3 > a")
titles = bs.find_all("div", {"class": "xrnccd"})

news = []

for i in titles:
    title = i.find("h3").text
    links = "https://news.google.com" + i.find("a")["href"][1:]
    data = i.find("time").text
    news.append([title, links, data])
    google_news_df = pd.DataFrame(news, columns=["기사 제목", "링크 주소", "게시 날짜"])

google_news_df.to_excel("뉴스 크롤링 결과2.xlsx")

print("저장성공!!!")
