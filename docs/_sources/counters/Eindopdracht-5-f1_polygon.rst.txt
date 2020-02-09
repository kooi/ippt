Eindopdracht hoofdstuk 5
::::::::::::::::::::::::

Als afsluiting van het hoofdstuk is hieronder een eindopdracht. Deel 1 van deze
opdracht is vergelijkbaar met vorige opdrachten -- je moet wederom een figuur
natekenen met tina -- al zal dit nu iets meer werk zijn. Deel 2 van de opdracht
voer je uit op moodle nadat je je code hebt ingeleverd. Je moet dan een paar
vragen over je gemaakte programma invullen.

Voor deze opdracht krijg je een beoordeling (``o``, ``t`` of ``v``). Als je
deze niet voldoende gemaakt hebt is er overigens wel de mogelijkheid een
herkansingsopdracht te maken.

Eindopdracht
------------

Maak nu het volgende figuur na. Belangrijk om te weten: Je begint met een
driehoek, vervolgens teken je een vierhoek, en dan een vijfhoek, en dan een
zeshoek. En je gaat door totdat je een negenhoek hebt. De zijden van alle
figuren zijn 50 pixels lang. Hint: Het kan in slechts 4 regels.

.. image:: images/polygon.png

.. activecode:: opg-counters-polygon
   :caption: Polygon
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)
