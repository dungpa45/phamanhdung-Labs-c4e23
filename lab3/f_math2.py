from random import randint,choice

op_list = ["+","-","*","/"]
op =choice(op_list)
# print(op)
a = randint(0, 10)
b = randint(0, 10)
err = choice([-2,-1,0,0,1,2,0])
dung = [a+b, a-b, a*b, a/b]
r = a + b + err

print(a,op, b, "=", r)

chon = input("Y / N  :")
if chon == "y":
    if r == dung:
        print("Bingo")
    else:
        print("fail")
elif chon == "n":
    if r != dung:
        print("Bingo")
    elif r == dung:
        print("fail")

