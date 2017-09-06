Oefenopdrachten (1)
:::::::::::::::::::::::::::


1. 5x tekenhuis()
-----------------

Teken m.b.v. de functie ``tekenhuis()`` en een loop vijf huizen naast elkaar. Zorg er wel voor dat deze op het scherm passen.

.. activecode:: oefen-functions-tekenhuis5
   :caption: 5x tekenen met tekenhuis()
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

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



2. Meer sterren
---------------

Teken het onderstaande plaatje na. Maak gebruik van de onderstaande code.

.. image:: images/sterren.png

.. activecode:: oefen-functions-tekenster3
   :caption: 3x een ster tekenen
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   def tekenster ():
       for i in range(12):
           tina.forward(50)
           tina.backward(50)
           tina.right(30)
