Oefenopdrachten (1): Korter
:::::::::::::::::::::::::::

Hieronder staan een aantal beginnetjes code en een voorbeeldfiguur. Pas de code telkens op zo'n manier aan dat de turtle de figuur tekent. De afmetingen staan in de figuur vermeld, die getallen hoef je er dus niet bij te zetten.


1. Inkorten
---------------

Voer het onderstaande programma uit en bekijk het resultaat. Kun jij het programma korter schrijven door gebruik te maken van een loop? *Hint: Er kunnen in totaat 9 regels minder.*

.. activecode:: oefen-iteration-hex
   :caption: Inkorten
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.forward(50)
   tina.right(60)
   tina.forward(50)
   tina.right(60)
   tina.forward(50)
   tina.right(60)
   tina.forward(50)
   tina.right(60)
   tina.forward(50)
   tina.right(60)
   tina.forward(50)
   tina.right(60)


2. Vierkant
---------------

Gebruik een loop om een vierkant te tekenen waarvan de zijden 200 pixels lang zijn. Er hoeven maar 3 regels bij.

.. activecode:: oefen-iteration-vierkant
   :caption: Vierkant
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
