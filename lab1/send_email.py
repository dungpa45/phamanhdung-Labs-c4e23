from gmail import GMail, Message
from random import choice
gmail = GMail("dungphamanh45@gmail.com","dung4597")

sickness_list = ["thuong han","kiet ly","tieu chay"]

template = '''
<p>Ch&agrave;o chủ tịch,</p>
<p>H&ocirc;m nay em ngủ dậy thấy rất mệt, b&aacute;c sỹ bảo em bị sa đ&igrave;</p>
<p>Chủ tịch cho em nghỉ nh&eacute; :))</p>
<p>Nh&acirc;n vi&ecirc;n của sếp</p>
'''
sickness = choice(sickness_list)
symptom = "dau bung"


content = template.replace("{{sick}}", sickness).replace("{{symptom}}",symptom)
message = Message("Don xin lam chu tich nuoc", to="yolovl.cf@gmail.com", html=content)

gmail.send(message)
