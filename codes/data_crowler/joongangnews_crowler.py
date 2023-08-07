import requests
from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article

article_links = []
# 기사 URL 모두 가져오는 코드 : 5016개가 전체임 가져올수 있는 코드(210페이지)
for i in range(1, 100):
    url = f"https://www.joongang.co.kr/politics?page={i}"

    # 페이지 요청
    response = requests.get(url)
    html_content = response.content

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_content, "html.parser")

    # 기사 링크 추출
    articles = soup.select("#story_list > li > div > h2 > a")
    for article in articles:
        link = article["href"]
        article_links.append(link)

print(len(article_links))

data = []
cnt = 0
num = 0
for link in article_links:
    article = Article(link, language='ko')
    article.download()
    article.parse()
    title = article.title
    content = article.text
    date = article.publish_date
    article_url = link
    data.append([title, date, content, article_url])
    cnt += 1
    if cnt % 500 == 0:
        num += 1
        df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])
        df.to_csv(f"joongang_articles{num}.csv", index=True)
        data = []
    if cnt == len(article_links):
        df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])
        df.to_csv("joongang_articles5.csv", index=True)



