import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import snscrape.modules.twitter as sntwitter
import pandas as pd
from time import sleep

PATH = './chromedriver'
driver = webdriver.Chrome()

driver.get('https://twitter.com/login')
subject = "Vipin Bhaskar"

sleep(5)

username = driver.find_element(By.NAME,'text')
username.send_keys('codingsvipin')
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(5)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("@TwitteR8318*&#")

sleep(5)

login = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]").click()

sleep(5)

driver.get("https://twitter.com/codingsvipin")

query = "cricket"
tweets = []
limit = 10
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('tweets.csv')

sleep(100)
print()
