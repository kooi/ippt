Kleuren
:::::::

Een mooie tekening is niet compleet zonder kleur. Bij deze tekeningen kun je twee aspecten kiezen, de kleur van de lijn (ofwel de "pen") en de opvulling. Beide zijn standaard zwart ("black").

De lijnkleur veranderen doe je net als het kiezen van een andere pen door op het moment dat je van kleur wilt wisselen het commando ``pencolor(<kleur>)`` te geven.


.. activecode:: vb-statements-colorsquare
   :caption: Gekleurd vierkant
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.forward(50)
   tina.left(90)
   tina.pencolor("green")
   tina.forward(50)
   tina.left(90)
   tina.pencolor("red")
   tina.forward(50)
   tina.left(90)
   tina.pencolor("orange")
   tina.forward(50)
   tina.left(90)


Je kunt ook je tekening met kleur opvullen. De kleur stel je op eenzelfde manier in als de penkleur (met het commando ``fillcolor(<kleur>)``) maar hier moet je tijdens het tekenen ook aangeven wanneer je begint met opvullen, dit doe je met ``begin_fill()``, en wanneer je stopt met opvullen, met ``end_fill()``. Probeer in het onderstaande voorbeeld deze commando's op andere plaatsen te zetten.


.. activecode:: vb-statements-colorsquare2
   :caption: Ingekleurd vierkant
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.fillcolor("green")
   tina.begin_fill()
   tina.forward(50)
   tina.left(90)
   tina.forward(50)
   tina.left(90)
   tina.forward(50)
   tina.left(90)
   tina.forward(50)
   tina.left(90)
   tina.end_fill()
