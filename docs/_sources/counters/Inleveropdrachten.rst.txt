Inleveropdrachten
:::::::::::::::::

opg-counters-spiraal
-----------------------------

Hieronder zie je een spiraal dat uit 400 strepen bestaat. Het allereerste streepje is 0 pixels lang. Vervolgens wordt een 90 graden hoek naar rechts gemaakt. Daarna een streepje van 1 pixel lang. Dan weer een 90 graden hoek naar rechts. Daarna een streepje van 2 pixels lang, et cetera.

Vul de functie ``tekenspiraal`` verder in opdat deze het bovenstaande plaatje zou tekenen met ``tekenspiraal(400)``.
Bij het testen van de code is het handiger om deze niet te testen met ``tekenspiraal(400)`` maar met bijvoorbeeld ``tekenspiraal(20)``, dit duur namelijk aanmerkelijk minder lang om uit te voeren.

.. image:: images/spiraal.png

.. activecode:: opg-functions-spiraal
   :caption: Een hele lange spiraal
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def tekenspiraal(aantal):
       tina.forward()

   tekenspiraal(20)


opg-counters-vierkanten
-----------------------

Maak nu een programma waarmee de turtle het figuurtje hieronder tekent. Het kleinste vierkant heeft zijden van 20 pixels en het grootste vierkant zijden van 95 pixels.
Maak vervolgens gebruik van de functie ``rndcol()`` om een elk vierkant een willekeurige kleur te geven. Je kunt dit gebruiken door ``pencolor()`` aan te roepen met de parameter ``rndcol()``, dus ``tina.pencolor( rndcol() )``.

.. image:: images/vierkanten.png

.. activecode:: opg-counters-vierkanten
   :caption: 10 vierkanten
   :nocodelens:
   :language: python

   import random
   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def rndcol():
       return [random.randint(0,255), random.randint(0,255), random.random(0,255)]


opg-counters-spiraal2
---------------------

Maak nu een programma waarmee je de volgende spiraal kan maken. Het eerste streepje is 10 pixels lang. De stappen zijn 5 pixels lang. De laatste streep is 195 pixels lang.

.. image:: images/spiraal2.png

.. activecode:: opg-counters-spiraal2
   :caption: Spiraal2
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)


opg-counters-polygon
---------------------

Maak nu het volgende figuur na. Belangrijk om te weten: Je begint met een driehoek, vervolgens teken je een vierhoek, en dan een vijfhoek, en dan een zeshoek. En je gaat door totdat je een negenhoek hebt. De zijden van alle figuren zijn 50 pixels lang. Hint: Het kan in slechts 4 regels.

.. image:: images/polygon.png

.. activecode:: opg-counters-polygon
   :caption: Polygon
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)
