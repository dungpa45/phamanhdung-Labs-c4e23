a = int(input("Nhap so a: "))
chon = input("Ban muon dung phep tinh nao +,-,*,/")
b = int(input("Nhap so b: "))

if chon=='+':
    print(a,"+",b,"=",a+b)
elif chon=='-':
    print(a,"-",b,"=",a-b)
elif chon=='*':
    print(a,"*",b,"=",a*b)
elif chon=='/':
    if a ==0 or b==0:
        print("vo nghiem")
    else:
        print(a,"/",b,"=",a/b)
else:
    print("ko co ho tro phep toan do")