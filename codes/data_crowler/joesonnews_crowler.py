import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼두기
chrome_options = Options()
"""
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
"""

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.chosun.com/politics/")

cnt = 0

"""# id가 something 인 element 를 찾음
some_tag = driver.find_element_by_id('something')

# somthing element 까지 스크롤
action = ActionChains(driver)
action.move_to_element(some_tag).perform()"""


# "기사 더보기" 버튼이 있는지 확인하고 계속 클릭
while cnt <= 200:
    try:
        driver.implicitly_wait(200)
        some_tag = driver.find_element(By.CLASS_NAME, "load-more-btn")
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        time.sleep(2)
        load_more_btn = driver.find_element(By.CLASS_NAME, "load-more-btn")
        load_more_btn.click()
        driver.implicitly_wait(200)
        cnt += 1
        print(cnt)
    except:
        break

article_url_list = []
data = []
num = 0

#bs4 코드
"""article_links = driver.find_elements(By.CSS_SELECTOR, "div.story-card-component > a.story-card__headline")
for link in article_links:
    article_url_list.append(link.get_attribute("href"))

print(article_url_list)

for link in article_url_list:
    driver.get(link)
    driver.implicitly_wait(20)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    title = soup.select_one(".article-header__headline > span").text.strip()
    content = soup.select_one("section.article-body").text.strip()
    date = soup.select_one("span.dateBox").text.strip()

    num+=1
    print(num)
    print(title)
    print(content)
    print(date)

    data.append([title, date, content, link])"""



#셀레늄 코드
driver.implicitly_wait(200)
time.sleep(2)
article_links = driver.find_elements(By.CSS_SELECTOR, "div.story-card-component > a.story-card__headline")
driver.implicitly_wait(200)
time.sleep(2)
for link in article_links:
    time.sleep(2)
    article_url_list.append(link.get_attribute("href"))
print(article_url_list)
print(len(article_url_list))

"""for link in article_url_list:
            driver.get(link)
            driver.implicitly_wait(10)
            title = driver.find_element(By.CSS_SELECTOR, ".article-header__headline > span").text
            content = driver.find_element(By.CSS_SELECTOR, "section.article-body").text
            date = driver.find_element(By.CSS_SELECTOR, "span.dateBox").text
            article_url = link
            data.append([title, date.split(" ")[1], content, article_url])

            num += 1
            print(num)
            print(title)
            print(content)
            print(article_url)


df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])

# 엑셀 파일로 내보내기
df.to_csv("articles01.csv")
"""