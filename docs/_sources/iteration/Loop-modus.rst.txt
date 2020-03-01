Loop-modus
::::::::::


Standaard is de turtle steeds in *pen-modus*. Dit betekent dat hij steeds een lijn aan het tekenen is terwijl hij beweegt. De turtle kan ook in *wandel-modus* terecht. Dan kan hij bewegen, terwijl hij geen spoor nalaat. Je kunt tijdens het uitvoeren van een programma meerdere keren naar pen-modus of wandel-modus.

Door het commando ``penup()`` in te geven kom je in *wandel-modus* terecht.
Door het commando ``pendown()`` in te geven kom je in *pen-modus* terecht.

Op deze manier kun je bijvoorbeeld een stippellijn tekenen.

.. activecode:: oefen-iteration-penup
   :caption: Stippellijn
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   for i in range(20):
       tina.forward(5)
       tina.penup()
       tina.forward(5)
       tina.pendown()
