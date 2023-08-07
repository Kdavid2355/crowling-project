from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import urllib.request
import ssl
import openpyxl
import time

ssl._create_default_https_context = ssl._create_unverified_context

# 내가 작업할 Workbook 생성하기
wb = openpyxl.Workbook()

# 작업할 Workbook 내 Sheet 활성화
sheet = wb.active

# Sheet 내 제목 설정
sheet.append(["순번", "기사제목", "기사url", "발행일자"])

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼두기
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options)
timeout = 4
#검색하고자 하는 키워드
keyword = input("검색키워드를 입력하세요 : ")

# 웹페이지 해당 주소 이동

cnt = 1
for i in range(1, 12):
    try:

        driver.get("https://search.news.cn/?lang=kr#search/0/{}/{}/".format(keyword, i))
        driver.refresh()
        driver.implicitly_wait(20)
        elements = driver.find_elements(By.CSS_SELECTOR, ".news")

        # 제목과 href 값 출력
        for element in elements:
            title = element.find_element(By.CSS_SELECTOR, "h2 > a").text
            href = element.find_element(By.CSS_SELECTOR, "h2 > a").get_attribute("href")
            date = element.find_element(By.CSS_SELECTOR, ".easynews .newstime > span").text
            print("순번", cnt)
            print("제목:", title)
            print("링크:", href)
            print("발행일자", date)
            print()
            sheet.append([cnt, title, href, date])
            cnt += 1
    except TimeoutException:
        print("종료!")
        break



# 작업 마친 후 파일 저장
wb.save("신화통신뉴스크롤링_일본.xlsx")