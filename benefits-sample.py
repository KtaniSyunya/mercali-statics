from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# プロファイルデータのPATHとユーザー名を指定
profile_path = r"プロファイル保存先のパス"
print("ユーザー情報の場所：", profile_path)
account_name = 'admin'

# ドライバ設定
options = Options()
options.add_argument('--lang=ja')
options.add_argument('--no-sandbox')
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument(f'--profile-directory={account_name}')

#売上履歴のページから売上を取得
driver = webdriver.Chrome(options=options)
driver.get("https://jp.mercari.com/mypage/sales_history")
time.sleep(1)

Earnings_list = []

Earnings  = driver.find_elements(by=By.CLASS_NAME, value="number__6b270ca7")
for i in Earnings:
    Earnings_list.append(i.text)

print(Earnings_list)
