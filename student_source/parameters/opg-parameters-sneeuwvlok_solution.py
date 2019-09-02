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
    for i in range(num):
        parallellogram(lengte)
        tina.right(360.0/num) # 360.0 zorgt voor cast van int naar float

sneeuwvlok(30, 6)
