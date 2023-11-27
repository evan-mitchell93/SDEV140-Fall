import turtle
import random
#create instance of Turtle class
t = turtle.Turtle()
t.screen.bgcolor('#e6e6fa')

#change the shape of the turtle
"""t.shape("turtle")
t.pencolor("blue")
t.speed(1)
#turn the turtle around
t.left(180)
t.forward(100)
t.penup()
t.left(90)
t.forward(100)

#draw square
t.penup()
t.goto(-50,50)
t.setheading(90)
t.pendown()
for x in range(4):
    t.forward(200)
    t.left(90)
for x in range(4):
    t.forward(200)
    t.right(90)"""

n = 5
l = 25

for count in range(n):
    t.fillcolor(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )
    t.begin_fill()
    for i in range(6):
        t.forward(90)
        t.left(300)
    t.end_fill()
    t.left(360/n)
#infinite loop exits on window close
turtle.mainloop()