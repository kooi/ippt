Oefenopdrachten (1)
:::::::::::::::::::::::::::


1. Driehoeken
-------------

Schrijf een programma waarmee je het volgende figuurtje natekent. Je moet uiteraard wel gebruikmaken van een loop.

.. image:: images/driehoeken.png

.. activecode:: oefen-counters-driehoeken
   :caption: Driehoeken
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def driehoek(lengte):
       for i in range(3):
           tina.forward(lengte)
           tina.right(120)
