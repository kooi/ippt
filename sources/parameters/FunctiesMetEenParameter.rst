Functies met een parameter
::::::::::::::::::::::::::

Hieronder staan een tweetal functies, ``tekenhuis()`` en ``tekenhuis2()``. ``tekenhuis()`` is een functie waarmee je een klein huisje kan maken met zijden van 50 pixels ``tekenhuis2()`` een functie waarmee je een groter huisje kan maken met zijden van 75 pixels.

.. activecode:: vb-parameters-tekenhuis2
   :caption: ``tekenhuis()`` en ``tekenhuis2()``
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def tekenhuis():
       tina.left(90)

       for i in range(4):
           tina.forward(50)
           tina.right(90)

       tina.forward(50)
       tina.right(30)
       tina.forward(50)
       tina.right(120)
       tina.forward(50)
       tina.right(30)
       tina.forward(50)
       tina.right(90)
       tina.forward(50)
       tina.right(180)

   def tekenhuis2():
       tina.left(90)

       for i in range(4):
           tina.forward(75)
           tina.right(90)

       tina.forward(75)
       tina.right(30)
       tina.forward(75)
       tina.right(120)
       tina.forward(75)
       tina.right(30)
       tina.forward(75)
       tina.right(90)
       tina.forward(75)
       tina.right(180)

   tekenhuis()
   tekenhuis2()

Als je kijkt naar het verschil tussen de twee bovenstaande functies, dan merk je dat er haast geen verschil is; het enige dat anders is, is het getal waarmee je aangeeft hoeveel pixels de turtle vooruit moet gaan! Waarom zouden we dan zoveel code moeten schrijven? Kan het niet korter?

Het antwoord is: **JA!**

Als je functies zoals ``forward``, ``backward``, ``right``, ``left`` aanroept, dan moet je tussen de haakjes iets opschrijven. Bij ``forward`` bijvoorbeeld, moet je aangeven hoeveel de turtle vooruit moet gaan. Je zegt daarom ``forward(100)`` om aan te geven, dat hij 100 pixels vooruit moet gaan. Zou het nou niet makkelijker zijn om ook onze tekenhuis functie zo slim te maken, dat we slechts ``tekenhuis(100)`` hoeven te zeggen, om een groter huis met zijden van 100 pixels te maken? En als we ``tekenhuis(50)`` zeggen, dat hij dan een kleiner huis maakt, et cetera. Dit doen we als volgt:


**Stap 1**

In de ``def`` zetten we eerst het woordje *lengte* tussen de haakjes (je mag ook een ander woord kiezen).

.. code-block:: python

   def tekenhuis(lengte):
       tina.left(90)

       for i in range(4):
           tina.forward(50)
           tina.right(90)

       tina.forward(50)
       tina.right(30)
       tina.forward(50)
       tina.right(120)
       tina.forward(50)
       tina.right(30)
       tina.forward(50)
       tina.right(90)
       tina.forward(50)
       tina.right(180)


**Stap 2**

Vervolgens vervangen we het getal dat we tussen forward hebben gezet door het woordje ``lengte``.

.. code-block:: python

   def tekenhuis(lengte):
       tina.left(90)

       for i in range(4):
           tina.forward(lengte)
           tina.right(90)

       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(120)
       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(90)
       tina.forward(lengte)
       tina.right(180)


**Stap 3**

Roep nu de functie aan met de gewenste lengte.

Wat er nu gebeurt:
Als je ``tekenhuis(100)`` opgeeft, dan wordt het woordje lengte gelijkgemaakt aan het getal 100. Overal waar lengte staat is dan eigenlijk 100.

.. activecode:: vb-parameters-tekenhuisparameter
   :caption: ``tekenhuis(lengte)``
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def tekenhuis(lengte):
       tina.left(90)

       for i in range(4):
           tina.forward(lengte)
           tina.right(90)

       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(120)
       tina.forward(lengte)
       tina.right(30)
       tina.forward(lengte)
       tina.right(90)
       tina.forward(lengte)
       tina.right(180)

   tekenhuis(100)


Probeer dit ook uit met andere getallen, je hoeft alleen het getal bij het aanroepen te veranderen.
