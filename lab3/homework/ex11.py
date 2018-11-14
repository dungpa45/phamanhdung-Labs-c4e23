def is_inside(a,b):
    if b[0] <= a[0] <= b[0] + b[2] and b[1] <= a[1] <= b[1] + b[3]:
        print("true")
    else:
        print("False")

is_inside([100,20],[30,34,5,6])
