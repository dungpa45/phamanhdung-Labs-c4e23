from random import randint,choice
from func_intro import eva

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    err = randint(-2,2)
    o = choice(["+","-","*","/"])
    r = eva(x, y, o) + err

    return x,y,o,r,err

a, b, op, r,err = generate_quiz()

print(a,op,b,"=",r)
chon = input("Y / N  :")
if chon =="y":
    if err == 0:
        print("Bingo")
    else:
        print("fail")
else:
    if err==0:
        print("Fail")
    else:
        print("Bingo")
