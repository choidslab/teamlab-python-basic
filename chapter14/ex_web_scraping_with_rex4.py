import urllib.request
import re

URL = "http://finance.naver.com/item/main.nhn?code=005930"

html = urllib.request.urlopen(URL)
html_contents = str(html.read().decode('ms949'))

stock_result = re.findall("(\<dl class=\"blind\">)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_result[0]
samsung_index = samsung_stock[1]
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
