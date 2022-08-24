# 403 Forbidden解決方法：https://blog.csdn.net/eric_sunah/article/details/11301873
# 與time相關網站
# https://officeguide.cc/python-time-tutorial-examples/
# https://www.geeksforgeeks.org/python-time-localtime-method/#:~:text=localtime()%20method%20of%20Time,the%20epoch%20to%20a%20time.

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

def crawl_website_data(bs):
    page_data = bs.find("div", "bbs-screen bbs-content").text
    print(page_data)


output = open("result.txt", "w", encoding='UTF-8')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) \
Gecko/20100101 Firefox/23.0"}
req = Request(url="https://www.ptt.cc/bbs/Railway/M.1658715508.A.2B5.html", headers=headers)
html = urlopen(req).read()

bs = BeautifulSoup(html, "html.parser")
data_set = crawl_website_data(bs)  # 把目前的這一頁抓下來
output.close()
