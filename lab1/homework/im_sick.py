from gmail import GMail, Message
from random import choice
import datetime
# from datetime import date
# from datetime import time


gmail = GMail("dungphamanh45@gmail.com", "dung4597")

sickness_list = ["thương hàn", "kiết lỵ", "tiêu chảy"]

template = '''
<p>Ch&agrave;o chủ tịch,</p>
<p>H&ocirc;m nay em ngủ dậy thấy rất mệt, b&aacute;c sỹ bảo em bị {{sick}}</p>
<p>Chủ tịch cho em nghỉ nh&eacute; :))</p>
<p>Nh&acirc;n vi&ecirc;n của sếp</p>
'''
sickness = choice(sickness_list)
symptom = "đau bụng"


content = template.replace(
    "{{sick}}", sickness).replace("{{symptom}}", symptom)
message = Message("Đơn xin nghỉ ốm", to="dphamanh45@gmail.com", html=content)


from datetime import datetime

now=datetime.time(datetime.now())
n=now.strftime("%H:%M")
timer="07:00"
while True:
    if timer<n:
        gmail.send(message)
        break
    
