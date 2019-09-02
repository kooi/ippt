import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

for i in range(3, 10, 1):
    for j in range(i):
        tina.forward(50)
        tina.left(360-360.0/i) # 360.0/i is een float
