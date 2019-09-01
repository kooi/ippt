import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def tekenhuis():
    tina.left(90)

    for i in range(4):
       tina.forward(50)
       tina.right(90)

    tina.forward(50)
    tina.right(30)
    tina.forward(50)
    tina.right(120)
    tina.forward(50)
    tina.right(30)
    tina.forward(50)
    tina.right(90)
    tina.forward(50)
    tina.right(180)

def rijhuizen():
    for i in range(5):
        tina.pendown()
        tekenhuis()
        tina.penup()
        tina.forward(75)

tina.penup()
tina.left(180)
tina.forward(180)
tina.right(90)
tina.forward(80)
tina.right(90)
for i in range (3):
    rijhuizen()
    tina.backward(375)
    tina.right(90)
    tina.forward(120)
    tina.left(90)
