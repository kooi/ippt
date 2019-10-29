:orphan:

Herkansing eindopdracht hoofdstuk 3
:::::::::::::::::::::::::::::::::::

Eindopdracht
------------

Eindopdracht
------------

Maak drie functies:

#. Een functie genaamd ``driehoek200()`` die een gele gelijkzijdige driehoek
   met zijden 200 tekent;
#. Een functie genaamd ``driehoek150()`` die een groene gelijkzijdige driehoek
   met zijden 150 tekent;
#. Een functie genaamd ``driehoek100()`` die een blauwe gelijkzijdige driehoek
   met zijden 100 tekent;
#. Als je dan achtereenvolgens ``driehoek200``, ``driehoek150`` en
   ``driehoek100`` aanroept ziet het eruit als hieronder.

.. image:: images/grotedriehoeken.png

.. activecode:: h3f2_driehoeken
  :caption: Driehoeksfuncties
  :nocodelens:
  :language: python
  :enabledownload:

  import turtle
  tina = turtle.Turtle()
  tina.shape("turtle")
