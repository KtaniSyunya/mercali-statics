# サンプルの一次元配列
cities = ["東京", "大阪", "名古屋", "京都"]
populations = [13750000, 2691000, 2295000, 1475000]

# zip関数で2つのリストを対応付け、その結果をリストに変換
paired_list = list(zip(cities, populations))

# "京" を含む要素のみをフィルタリング
filtered_list = [pair for pair in paired_list if "京" in pair[0]]

# "京" を含む都市の人口を合計
total_population = sum([population for city, population in filtered_list])

print(f'"京" を含む都市の合計人口: {total_population}')