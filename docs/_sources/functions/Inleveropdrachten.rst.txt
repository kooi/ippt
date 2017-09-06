Inleveropdrachten
:::::::::::::::::

opg-functions-grotevierkanten
-----------------------------

Maak drie functies. Een functie genaamd ``vierkant100()`` die een vierkant met zijden van 100 pixels tekent. Een functie genaamd ``vierkant150()`` die een vierkant met zijden van 150 pixels tekent. En een functie genaamd ``vierkant200()`` die een vierkant met zijden van 200 pixels tekent. Roep alle drie de functies vervolgens achter elkaar aan. Het resultaat moet er als volgt uitzien:

.. image:: images/grotevierkanten.png

.. activecode:: opg-functions-grotevierkanten
   :caption: Vierkantfuncties
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   vierkant100()
   vierkant150()
   vierkant200()


opg-functions-rijhuizen
-----------------------

Teken de onderstaande figuur. Maak eerst een functie ``rijhuizen()`` af die 5 huizen naast elkaar tekent en roep die 3x aan zodat er een heel dorp getekend wordt. Omdat dit anders heel erg lang zou duren is op regel vier een nieuw commando bijgevoegd. Met het commando ``speed()`` kun je de turtle sneller laten gaan.

.. image:: images/rijhuizen.png

.. activecode:: opg-functions-rijhuizen
   :caption: Nog meer huizen
   :nocodelens:
   :language: python

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

   def rijhuizen():
       for i in range(5):
           tekenhuis()


opg-functions-gekleurdedraaiendevierkanten
------------------------------------------

Teken de onderstaande figuur na. Maak gebruik van de functie ``maakvierhoek()``.

.. image:: images/coloredsquares.png

.. activecode:: opg-functions-gekleurdedraaiendevierkanten
   :caption: Regenboogvierkanten
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   def maakvierhoek():
       for i in range(4):
           tina.right(90)
           tina.forward(100)
