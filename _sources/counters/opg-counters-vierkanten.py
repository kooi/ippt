import random
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def rndcol():
    return [random.randint(0,255), random.randint(0,255), random.random(0,255)]
