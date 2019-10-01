Opdracht 3-2: Veel huizen
:::::::::::::::::::::::::

Opdracht
--------

#. Gebruik de functie ``tekenhuis()`` en een loop om 5x een huis te tekenen.
#. Pas de functie ``tekenhuis()`` op zo'n manier aan dat elk huis een rood
   dak krijgt.

Teken m.b.v. de functie ``tekenhuis()`` en een loop vijf huizen naast elkaar. Zorg er wel voor dat deze op het scherm passen.

.. activecode:: h3o2_veel-huizen
   :caption: 5x tekenen met tekenhuis()
   :nocodelens:
   :language: python
   :enabledownload:

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
