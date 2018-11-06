import turtle
import math

r = int(input())#지름.

wn = turtle.Screen()
wn.title('Triangle in Circle')
wn.setup(1000,1000)

def TA(tt,r):
    tt.left(60)
    for _ in range(3):
        tt.forward(math.sin(math.pi/3)*r)
        tt.left(120)
    tt.right(60)

t1 = turtle.Turtle()

t1.circle(r/2)
TA(t1,r)

t1.penup()
t1.goto(0,r)
t1.pendown()

t1.left(180)
TA(t1,r)

wn.mainloop()
