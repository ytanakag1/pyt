import requests
import json
import re
from bs4 import BeautifulSoup
from pprint import pprint

# Webページを取得して解析する
load_url = "https://page.auctions.yahoo.co.jp/jp/auction/v1020816649"
# html = requests.get(load_url)
data = {'test': 'bodydata'}
html = requests.get(load_url, data=json.dumps(data))

soup = BeautifulSoup(html.content, "html.parser")

reg_obj = re.compile(r"<[^>]*?>") #全てのタグの正規表現
# classで検索し、その中のすべてのaタグを検索して表示する
topic = soup.find(class_="Price__value")
pprint(topic)
topic = reg_obj.sub("", topic.text) #タグの除去
idx = topic.find('円')
topic = topic[:idx]  # スライスで円よりも前を抽出
topic = topic.replace(',','') #カンマ除去
print(topic)
