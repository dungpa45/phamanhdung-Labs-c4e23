from turtle import *
shape("turtle")
speed(0)

def draw_square(length,colors):
    color(colors)
    
    for i in range(4):
        forward(length)
        left(90)  

# draw_square(90,'red')

#turtle 4
for i in range(30):
    length = draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()

