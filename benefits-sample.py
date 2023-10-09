from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# ログイン画面URL
url = "https://login.jp.mercari.com/signin?params=client_id%3DbP4zN6jIZQeutikiUFpbx307DVK1pmoW%26code_challenge%3DD8k7fwRsuFP-NJxTR60f5FJP1jYhLmBaxyTKgkCfZns%26code_challenge_method%3DS256%26nonce%3DnZ4ALynO-5IW%26redirect_uri%3Dhttps%253A%252F%252Fjp.mercari.com%252Fauth%252Fcallback%26response_type%3Dcode%26scope%3Dmercari%2520openid%26state%3DeyJwYXRoIjoiLyIsInJhbmRvbSI6InVjaVBqNDdvTjc2NiJ9%26ui_locales%3Dja"

# chromedriverの設定とキーワード検索実行
browser = webdriver.Chrome()
browser.get(url)
USER = "XXXXXXX"
PASS = "XXXXXXX"

elem_username  = browser.find_element(By.NAME, "emailOrPhone")
elem_username.send_keys(USER)
elem_password = browser.find_element(By.NAME, "password")
elem_password.send_keys(PASS)
time.sleep(5)

browser_from = browser.find_element(By.CLASS_NAME,"merButton")
browser_from.click()
print("ログイン成功です!")
time.sleep(30)




#/Users/kottani/Library/Application Support/Google/Chrome/Profile 1