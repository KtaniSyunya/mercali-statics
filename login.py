from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


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

#ログイン後に開く画面
driver = webdriver.Chrome(options=options)
driver.get("ログイン後のページURL")
time.sleep(40)