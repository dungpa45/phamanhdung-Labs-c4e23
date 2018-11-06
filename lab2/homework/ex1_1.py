from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1 connect to website
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

#2 Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf-8")


#3 find ROI region
soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul","")  # href="",id=""
# print(ul.prettify())

# 4 Extract data
li_list = ul.find_all("li")

itune_list = []
for li in li_list:

    # li = li_list[0]
    a = li.a
    h3 = li.h3
    h4 = li.h4
    # print(a.string)
    title = h3.string
    singer = h4.string
    link = url+a["href"]

    itune = OrderedDict({
        "title": title,
        "singer": singer,
        "link": link,
    })
    itune_list.append(itune)
# print(itune_list)

#5 save data
pyexcel.save_as(records=itune_list, dest_file_name="Itune_top_song.xlsx")
