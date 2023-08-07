import tweepy
import keys
from bs4 import BeautifulSoup
import requests
import schedule
from datetime import datetime

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

def get_blood_info():
    url = "https://www.bloodinfo.net/knrcbs/main.do"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    infos = soup.select("#blood_notice1 > div.blood_list > ul > li > p.num")

    blood_info = [info.text for info in infos]
    return blood_info

def tweet():
    blood_info = get_blood_info()
    date = datetime.now().strftime('%Y년 %m월 %d일')
    tweet_text = f"{date} 혈액보유량입니다. \n A형 {blood_info[0]}일, B형 {blood_info[1]}일, O형 {blood_info[2]}일, AB형 {blood_info[3]}일"
    client.create_tweet(text=tweet_text)
    print(f"Tweeted at {datetime.now().ctime()}: {tweet_text}")

# 매일 오후 3시에 트윗하도록 설정
schedule.every().day.at("13:57").do(tweet)

while True:
    schedule.run_pending()
