Programmeren
::::::::::::

Een eenvoudige definitie van programmeren is dat je de computer meerdere opdrachten geeft die hij achterelkaar dient uit te voeren.

Hieronder een eerste programma dat je in Python kan uitvoeren:

.. activecode:: vb-statements-prog
   :caption: Tina volgt een pad
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.left(90)
   tina.forward(50)
   tina.right(90)
   tina.forward(75)
   tina.right(90)
   tina.forward(25)
   tina.left(90)
   tina.forward(75)
   tina.right(90)
   tina.forward(25)
