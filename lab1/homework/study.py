
print("Learn how to get the current hour of your computer")

import datetime
now = datetime.datetime.now()
print("Giờ",now.hour, now.minute, now.second,sep=":")
print("Ngày", now.day,"Tháng",now.month,"Năm", now.year)
