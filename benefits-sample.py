from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

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

#売上履歴ページ取得
driver = webdriver.Chrome(options=options)
driver.get("https://jp.mercari.com/mypage/sales_history")
time.sleep(1)

Earnings_list = []
contents_list = []

#売上履歴における各コンテンツ料金取得
Earnings  = driver.find_elements(by=By.CLASS_NAME, value="number__6b270ca7")
for i in Earnings:
    Earnings_list.append(i.text)

#売上履歴におけるコンテンツ取得
Earnings_list = [int(value.replace(',', '')) for value in Earnings_list]
length = len(Earnings_list) #売上履歴数

contents = driver.find_elements(by=By.CLASS_NAME, value="content__884ec505")
for i in contents:
    contents_list.append(i.text)
    contents_list
contents_list = contents_list[23:]

earninges = []
earninges = list(zip(contents_list,Earnings_list))

#検索したい年・月の入力
search_year = input("検索する年を入力してください(××××年)")
search_month = input("検索する月を入力してください(××月)")

filtered_list = [pair for pair in earninges if "販売利益\n"+str(search_year)+"/"+str(search_month) in pair[0]]
print(filtered_list)

#販売利益の合計
total_benefits = sum([earninge for content, earninge in filtered_list])

print(f""+str(search_year)+"年"+str(search_month)+"月合計販売利益："+str(total_benefits)+"円")
