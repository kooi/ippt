Opdracht 4-2: Driehoek
::::::::::::::::::::::

Hieronder staat een voorbeeldfiguur en een beginnetje van een programma. Pas de
code aan zodat tina de figuur tekent. De getallen die in de figuur staan zijn
afmetingen, deze hoef je uiteraard niet in jouw tekening erbij te zetten.

Als een geheugensteuntje staat een samenvatting van de programmeercodes die je
tot nu toe geleerd hebt hieronder.

Als je klaar bent sla je je programma op door op ``download`` te drukken en dan
lever je dit bestand in via moodle.


Opdracht
--------


Maak een functie ``driehoek()`` die driehoeken van verschillende lengtes kan tekenen. Uiteindelijk moet je drie driehoeken tekenen. Één met zijden van 20 pixels, één met zijden van 40 pixels en één met zijden van 60 pixels. Het moet er als volgt uitzien:

.. image:: images/driehoeken.png

.. activecode:: h4o2_driehoek
   :caption: ``driehoek()``
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   # zet hier de code voor de definitie van driehoek()

   driehoek(20)
   tina.penup()
   tina.forward(50)
   tina.pendown()
   driehoek(40)
   tina.penup()
   tina.forward(50)
   tina.pendown()
   driehoek(60)
