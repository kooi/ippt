Oefenopdrachten (2): Kleuren
::::::::::::::::::::::::::::

Hieronder staan een aantal beginnetjes code en een voorbeeldfiguur. Pas de code telkens op zo'n manier aan dat de turtle de figuur tekent. De afmetingen staan in de figuur vermeld, die getallen hoef je er dus niet bij te zetten.


1. Gekleurde driehoek
---------------------

.. image:: images/triangle-blue.png

.. activecode:: oefen-statements-driehoekkleur
   :caption: Gekleurde driehoek
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.fillcolor("light blue")
   tina.begin_fill()
   tina.forward(100)
   tina.left(120)


2. Gekleurde driehoek
---------------------

.. image:: images/parallelogram-green.png

.. activecode:: oefen-statements-parallelogramkleur
   :caption: Gekleurd parallelogram
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.fillcolor("")
   tina.begin_fill()
   tina.forward(100)
   tina.left(60)


3. Gekleurde ruit
---------------------

.. image:: images/diamond-red.png

.. activecode:: oefen-statements-ruitkleur
   :caption: Gekleurde ruit
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.pencolor("")
   tina.fillcolor("")
   tina.begin_fill()
   tina.left(120)
   tina.forward(100)


4. Gekleurd hexagon
---------------------

.. image:: images/hexagon-yellow.png

.. activecode:: oefen-statements-hexagonkleur
   :caption: Gekleurd hexagon
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.pencolor("")
   tina.fillcolor("")
   tina.begin_fill()
   tina.left(120)
   tina.forward(100)
