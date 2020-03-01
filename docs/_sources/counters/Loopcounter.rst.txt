Loopcounter
:::::::::::

Allereerst is het belangrijk om te weten dat we i.p.v. ``i`` ook een andere naam hadden kunnen kiezen. De meeste programmeurs gebruiken vaak een letter zoals ``j``, ``k``, ``x``, maar ook het woordje ``count``. De gouden is blijft "een gepaste naam dat overeenkomt met de bedoeling ervan".

Deze ``i`` wordt ook wel de *loopcounter* of de teller genoemd. Tijdens het herhalen wordt hiermee bijgehouden bij welke herhaling de computer is! De eerste keer dat de loop herhaalt, is ``i`` gelijk aan het getal 0. De tweede keer wordt hij 1. De derde keer wordt hij 2 en de vierde keer wordt hij gelijk aan 3. En dan houdt de loop op. Wat kun je hier nu mee? Nou, een hele hoop! Laten we eerst een eenvoudig voorbeeld nemen. We gebruiken hier de functie ``dot(<grootte>)``, deze tekent een stip van de meegegeven ``<grootte>`` op de plek waar de turtle is.

.. activecode:: vb-counters-stippen
   :caption: Een aantal stippen
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   for i in range(10):
       tina.dot(1)
       tina.penup()
       tina.forward(10)
       tina.pendown()


Dit programma tekent 10 stippen achter elkaar. De dikte van elke stip is 1 pixel. Nadat hij een pixel heeft getekend, schuift de turtle 10 pixels op. En dat wordt 10 keer herhaald.

Bij elke herhaling gebeurt nu hetzelfde. Maar stel dat je na elke herhaling de stip 1 pixel groter wilt maken. Hoe doe je dat dan?

Omdat de ``i`` na elke herhaling eentje groter wordt kunnen we dat goed gebruiken. We vervangen de 1 van ``dot(1)`` met ``i``. Dat ziet er dan als volgt uit:

.. activecode:: vb-counters-stippen2
   :caption: Wederom een aantal stippen
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   for i in range(10):
       tina.dot(i)
       tina.penup()
       tina.forward(10)
       tina.pendown()


Probeer ook in het bovenstaande voorbeeld ook ``forward(10)`` te vervangen door ``forward(i)``.
Of de ``i`` te vervangen door ``i * 2``?
