Opdracht 2-1: Inkorten
::::::::::::::::::::::

Voer het onderstaande programma uit en bekijk het resultaat. Kun jij het
programma korter schrijven door gebruik te maken van een loop?
*Hint: Er kunnen in totaat 9 regels minder.*

Als een geheugensteuntje staat een samenvatting van de  programmeercodes die je
tot nu toe dit hoofdstuk geleerd hebt hieronder.


Opdracht
--------

.. activecode:: h2o1_inkorten
   :caption: Inkorten
   :nocodelens:
   :language: python
   :enabledownload:

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


Samenvatting (2-1)
------------------

.. code-block:: python

   for i in range(<aantal>):
       <code>

herhaal de <code> <aantal> keer
