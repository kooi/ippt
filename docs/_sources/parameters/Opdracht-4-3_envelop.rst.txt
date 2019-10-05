Opdracht 4-3: Gekleurde envelop
:::::::::::::::::::::::::::::::

Hieronder staat een voorbeeldfiguur en een beginnetje van een programma. Pas de
code aan zodat tina de figuur tekent. De getallen die in de figuur staan zijn
afmetingen, deze hoef je uiteraard niet in jouw tekening erbij te zetten.

Als een geheugensteuntje staat een samenvatting van de programmeercodes die je
tot nu toe geleerd hebt hieronder.

Als je klaar bent sla je je programma op door op ``download`` te drukken en dan
lever je dit bestand in via moodle.


Opdracht
--------

Maak een functie ``envelop()`` die de parameters ``lengte``, en ``kleur``
meekrijgt. Hieronder zijn een paar voorbeelden van hoe het eruit moet zien.

.. image:: images/gekleurde_envelop.png

.. activecode:: h4o3_envelop
   :caption: envelop()
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   # definitie van de functie envelop() hier invullen

   envelop(50, "red")
   envelop(100, 'green')
