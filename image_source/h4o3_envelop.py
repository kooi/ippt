import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(10)

def envelop(lengte, kleur):
    tina.pencolor(kleur)
    for i in range(4):
        tina.forward(lengte)
        tina.right(90)
    for i in range(3):
        tina.forward(lengte)
        tina.right(120)
    tina.penup()
    tina.right(90)
    tina.forward(lengte+10)
    tina.write('envelop('+str(lengte)+',"'+kleur+'")')
    tina.backward(lengte+10)
    tina.left(90)
    tina.pendown()

    
for x,y,s,c in [(-150,150,50,'red'), 
                (50,150,100,'green'), 
                (-150,50, 150, 'purple'),
                (75, 0, 25, 'blue')]:
    tina.penup()
    tina.goto(x, y)
    tina.pendown()
    envelop(s, c)
