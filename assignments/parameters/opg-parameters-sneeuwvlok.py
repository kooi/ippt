import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def parallellogram(lengte):
    for i in range(2):
        tina.forward(lengte)
        tina.right(60)
        tina.forward(lengte)
        tina.right(120)

def sneeuwvlok(lengte, num):
    parallellogram(lengte)

sneeuwvlok(30, 6)
