from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1 connect to website
url = "https://dantri.com.vn"
conn = urlopen(url)

#2 Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf-8")
# print(page_content)

# with open("dantri.html","wb") as f:
#     f.write(raw_data)

#3 find ROI region
soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew") #href="",id=""
# print(ul.prettify())

#4 Extract data
li_list = ul.find_all("li")  

news_list =[]
for li in li_list:

# li = li_list[0]
    a = li.h4.a
    # print(a.string)
    title = a.string
    link = url+a["href"]
    
    news = OrderedDict({
        "title":title,
        "link":link,
    })
    news_list.append(news)
    # print(news)

#5 save data

pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
