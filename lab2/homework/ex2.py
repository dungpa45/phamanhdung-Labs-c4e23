from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1 connect to website
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

#2 Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf-8")

#3 find ROI region
soup = BeautifulSoup(page_content, "html.parser")

table = soup.find("table", id="tableContent")  # href="",id=""
# print(table.prettify())

# 4 Extract data
tr_list = table.find_all("tr")
# print(tb_list)
baocao_list = []
for tr in tr_list:
    td_list = tr.find_all("td")
    dic={}
    for i in range(len(td_list)):
        if td_list[i].string != None:
            if i == 0:
                dic["Danh Mục"] = td_list[i].string.strip()
            elif i == 1:
                dic["Qúy 4-2016"] = td_list[i].string.strip()
            elif i == 2:
                dic["Quý 1-2017"] = td_list[i].string.strip()
            elif i == 3:
                dic["Quý 2-2017"] = td_list[i].string.strip()
            elif i == 4:
                dic["Quý 3-2017"] = td_list[i].string.strip()
    
    print(dic)
    if dic !={}:
        baocao_list.append(dic)

# #5 save data
pyexcel.save_as(records=baocao_list, dest_file_name="Bao_cao_tai_chinh_cty_sua_vn.xlsx")
