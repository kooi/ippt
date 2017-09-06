Oefenopdrachten (1)
:::::::::::::::::::::::::::


1. vierkant()
-------------

Maak een functie vierkant waarin je tussen de haakjes kan aangeven hoe groot het vierkant moet zijn. Je moet de functie dus als het volgt kunnen gebruiken:

.. code-block:: python

   vierkant(20)
   vierkant(50)
   vierkant(100)

et cetera.


.. activecode:: oefen-parameters-vierkanten
   :caption: ``vierkant()``
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def vierkant():
       for i in range(4):
           tina.forward(50)
           tina.right(90)

   vierkant(20)
   vierkant(50)
   vierkant(100)


2. driehoek()
---------------

Maak een functie ``driehoek()`` die driehoeken van verschillende lengtes kan tekenen. Uiteindelijk moet je drie driehoeken tekenen. Één met zijden van 20 pixels, één met zijden van 40 pixels en één met zijden van 60 pixels. Het moet er als volgt uitzien:

.. image:: images/driehoeken.png

.. activecode:: oefen-parameters-driehoeken
   :caption: ``driehoek()``
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   # zet hier de code voor de definitie van driehoek()

   driehoek(20)
   tina.penup()
   tina.forward(50)
   tina.pendown()
   driehoek(40)
   tina.penup()
   tina.forward(50)
   tina.pendown()
   driehoek(60)
