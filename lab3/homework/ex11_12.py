def is_inside(a,b):
    return b[0] <= a[0] <= b[0] + b[2] and b[1] <= a[1] <= b[1] + b[3]
    #     print("true")
    # else:
    #     print("False")

d=is_inside([200,120],[30,34,5,6])
if d == True:
    print("Your function is correct")
else:
    print("Oops, there's a bug")
