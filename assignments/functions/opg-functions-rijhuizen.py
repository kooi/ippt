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
        tekenhuis()
