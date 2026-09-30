from turtle import *
from random import randint

t3 = Turtle()

t3.speed(10)

t3.penup()
t3.goto(-140, -150)
t3.pendown()
t3.left(90)

for i in range(8):
    t3.forward(400)
    t3.right(90)
    t3.penup()
    t3.forward(20)
    t3.right(90)
    t3.pendown()
    t3.forward(400)

    t3.penup()
    t3.left(90)
    t3.forward(20)
    t3.pendown()
    t3.left(90)



t3.pendown()
t3.forward(400)
t3.hideturtle()   

finish = 200
def startRace(t, x, y, color):
    t.color(color)
    t.shape('turtle')
    t.penup()
    t.goto(x, y)

t1 = Turtle()
t2 = Turtle()
t4 = Turtle()

startRace(t1, -150, -20, 'green')
startRace(t2, -150, 20, 'purple')
startRace(t4, -150, 60, 'red')

while t1.xcor() < finish and t2.xcor() < finish and t4.xcor() < finish:
    t1.forward(randint(2, 7))
    t2.forward(randint(2, 7))
    t4.forward(randint(2, 7))
max_x = max(t1.xcor(), t2.xcor(), t4.xcor() )
t3.clear()

if max_x == t1.xcor():
    t1.goto(0, 0)   
    t1.pendown()
    for i in range (20):
        t1.left(20)
        t1.circle(40)
elif max_x == t2.xcor():
    t2.goto(0, 0)
    t2.pendown()
    for i in range (20):
        t2.left(20)
        t2.circle(40)
else:
    t4.goto(0, 0)
    t4.pendown()
    for i in range (20):
        t4.left(20)
        t4.circle(40)

