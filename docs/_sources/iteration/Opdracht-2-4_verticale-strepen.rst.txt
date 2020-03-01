Opdracht 2-4: Verticale strepen
:::::::::::::::::::::::::::::::

Hieronder staat een voorbeeldfiguur en een beginnetje van een programma. Pas de
code aan zodat tina de figuur tekent. De getallen die in de figuur staan zijn
afmetingen, deze hoef je uiteraard niet in jouw tekening erbij te zetten.

Als een geheugensteuntje staat een samenvatting van de  programmeercodes die je
tot nu toe dit hoofdstuk geleerd hebt hieronder.


Opdracht
--------

Schrijf een zo kort mogelijk programma dat de onderstaande tekening maakt.

.. image:: images/verticale-strepen.png

.. activecode:: h2o3_verticale-strepen
   :caption: Verticale strepen
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")


Samenvatting (2-2)
------------------

.. code-block:: python

   for i in range(<aantal>):
       <code>

herhaal de <code> <aantal> keer

``penup()``
  wandel-modus; turtle beweegt zonder te tekenen
``pendown()``
  schrijf-modus; turtle beweegt met tekenen
