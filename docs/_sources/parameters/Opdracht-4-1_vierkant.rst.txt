Opdracht 4-1: Vierkant
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

Maak een functie vierkant waarin je tussen de haakjes kan aangeven hoe groot het vierkant moet zijn. Je moet de functie dus als het volgt kunnen gebruiken:

.. code-block:: python

   vierkant(20)
   vierkant(50)
   vierkant(100)

et cetera.


.. activecode:: h4o1_vierkant
   :caption: ``vierkant()``
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def vierkant():
       for i in range(4):
           tina.forward(50)
           tina.right(90)

   vierkant(20)
   vierkant(50)
   vierkant(100)
