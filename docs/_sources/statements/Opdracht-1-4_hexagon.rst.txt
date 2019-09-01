Opdracht 1-4: Gekleurde hexagon
:::::::::::::::::::::::::::::::

Hieronder staat een voorbeeldfiguur en een beginnetje van een programma. Pas de
code aan zodat tina de figuur tekent. De getallen die in de figuur staan zijn
afmetingen, deze hoef je uiteraard niet in jouw tekening erbij te zetten.

Als een geheugensteuntje staat een samenvatting van de  programmeercodes die je
tot nu toe geleerd hebt hieronder.

Als je klaar bent sla je je programma op door op ``download`` te drukken en dan
lever je dit bestand in via moodle.


Opdracht
--------

.. image:: images/hexagon-yellow.png

.. activecode:: oefen-statements-hexagonkleur
   :caption: Gekleurd hexagon
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.pencolor("")
   tina.fillcolor("")
   tina.begin_fill()
   tina.left(120)
   tina.forward(100)


Samenvatting (1-2)
------------------

``pencolor(<kleur>)``
  verander de lijnkleur naar <kleur>. Gebruik hiervoor de Engelse naam voor de
  kleur tussen aanhalingstekens, bijvoorbeeld ``"red"``, ``"orange"``,
  ``"green"``, ``"pink"`` of ``"yellow"``.
``fillcolor(<kleur>)``
  verander de opvullingskleur
``begin_fill()``
  begin vanaf hier op te vullen
``end_fill()``
  stop hier met opvullen
