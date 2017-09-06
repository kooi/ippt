Oefenopdrachten (2)
:::::::::::::::::::::::::::


1. tekenhuis(lengte, kleur)
---------------------------

Breid de tekenhuis functie uit met een extra parameter waarmee je, naast de lengte, ook de kleur van de rand van het huisje kan meegeven.

.. activecode:: oefen-functions-tekenhuislengtekleur
   :caption: tekenhuis(lengte, kleur)
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def tekenhuis(lengte):
       tina.left(90)

       for i in range(4):
           tina.forward(lengte)
           tina.right(90)

       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(120)
       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(90)
       tina.forward(lengte)
       tina.right(180)

   tekenhuis(50)


2. rechthoek(lengte, breedte)
-----------------------------

Maak nu een functie genaamd rechthoek die twee parameters meekrijgt: *lengte* en *breedte*. Roep ten slotte de functie als volgt aan:

.. code-block:: python

   rechthoek(10,20)
   rechthoek(1,10)


.. activecode:: oefen-functions-rechthoek
   :caption: tekenhuis(lengte, kleur)
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   # zet hier de definitie van rechthoek()

   rechthoek(10,20)
   rechthoek(1,10)
