import turtle
tina = turtle.Turtle()
tina.shape("turtle")

def maakvierhoek():
    for i in range(4):
        tina.right(90)
        tina.forward(100)

for c in ["red", "orange", "yellow", "green", "blue", "violet" ]:
    tina.pencolor(c)
    maakvierhoek()
    tina.left(60)
