from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://instagram.com")

#인스타그램 자동로그인
driver.implicitly_wait(10)  #나타날때까지 최대 10초동안 기다려
login_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
login_id.send_keys('becreative_2028') # 아이디 입력
login_pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
login_pwd.send_keys('Bethebest22!')
driver.implicitly_wait(10)
login_id.send_keys(Keys.ENTER) #enter 키를 쳐주세요


time.sleep(5) #로그인하고 기다려야 로그인 정보가 웹에 남음 implicitly_wait 하면 바로 가버려서, 로그인 하라고 뜸
#페이지 이동
driver.get('https://www.instagram.com/explore/tags/%EB%8F%85%EC%84%9C%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8/')

driver.implicitly_wait(15)
#첫번째 사진 누름
first_img = driver.find_element(By.CSS_SELECTOR, '._aagw').click() #만약에 두번째 있는 사진부터 하고 싶다면, find_elements 쓰고, 인덱싱 하면 됨

driver.implicitly_wait(15)

for i in range(10):
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, '._aamw ._abl-')

        if like_button.is_enabled():
            print("좋아요 이미 눌러져 있습니다. 넘어갑니다.")
        else:
            like_button.click()
            print("좋아요 버튼을 클릭했습니다.")

        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()

    except:
        print("좋아요버튼이 없습니다.")
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()

'''
for i in range(10):
    driver.find_element(By.CSS_SELECTOR, '._aamw ._abl-').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
'''
'''
for i in range(50):
    try:
        #사진 저장
        img_element = driver.find_element(By.CSS_SELECTOR, '._aatk .x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
        img_src = img_element.get_attribute('src')
        urllib.request.urlretrieve(img_src, f'{i}.jpg')

        #다음 버튼 클릭하기
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
    except:
        # 다음 버튼 클릭하기
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()

'''