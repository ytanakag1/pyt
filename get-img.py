#url指定でページ内の画像をすべて保存する
import requests
import json
import re
import urllib
import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path
from pprint import pprint


load_url = "https://取得したいURL"
html = requests.get(load_url)
# pprint(html) ステータスコードが見れるだけ
soup = BeautifulSoup(html.content, "html.parser")

# uploads = Path("uploads") 
# uploads.mkdir(exist_ok=True) #一番上

category_folder = ''
year_folder = ''

for element in soup.find_all("img"):
    src = element.get("src")
    # pprint(src)
    image_url = urllib.parse.urljoin(load_url, src) #絶対パス
    imgdata = requests.get(image_url)

    pprint(len(image_url.split("/")))
    pprint(image_url.split("/"))
    sys.exit()

    # public/images/selling1.jpg
    if image_url.split("/")[-4] :
        pprint(image_url.split("/")[-4])
        category = image_url.split("/")[-4] #
        category_folder = Path(category) 
        os.makedirs(category_folder, exist_ok=True) #作られた

    # public/images/category/category-1.jpg
    if image_url.split("/")[-3] : 
        year = image_url.split("/")[-3] #
        year_folder = Path(category,year) 
        os.makedirs(year_folder, exist_ok=True) #作られた
    
    if image_url.split("/")[-2]: 
        month = image_url.split("/")[-2] 
        month_folder = Path(category,year,month)
        os.makedirs(month_folder , exist_ok=True)

    filename = image_url.split("/")[-1] #ファイル名だけ取り出す
    out_path = Path(category, year, month, filename)

    #ファイルに書き出す
    with open(out_path, mode="wb") as f:
        f.write(imgdata.content)
    print(image_url)
