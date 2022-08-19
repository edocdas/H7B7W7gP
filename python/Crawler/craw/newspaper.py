from bs4 import BeautifulSoup
from urllib.request import urlopen

pre = "https://udndata.com/library/"
url = "https://udndata.com/ndapp/Story?no=1&page=1&udndbid=udndata&SearchString=JiMzMjg3OTsmIzIxNTEyOyYjMjI1Nzc7K6TptME%2BPTIwMjIwNjE1K6TptME8PTIwMjIwNzE0K7P4p089wXCmWLP4fLhnwNmk6bP4fMFwplix37P4fFVwYXBlcg%3D%3D&sharepage=20&select=1&kind=2&article_date=2022-07-14&news_id=10031876"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) \
Gecko/20100101 Firefox/23.0"}
pre_html = urlopen(pre)
html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")
bs2 = BeautifulSoup(pre_html, "html.parser")
# print(bs)
print(bs2)