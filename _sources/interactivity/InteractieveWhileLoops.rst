Nog een keer loops, maar dan interactieve while loops
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Hiervoor heb je geleerd hoe loops werken. Als je wilt dat iets tien keer wordt herhaald, dan gebruik je de ``for``-loop. Hier een voorbeeld:

.. activecode:: vb-interactivity-for-loop
   :caption:
   :nocodelens:
   :language: python

   for i in range(10):
       print ("Dit is herhaling " + str(i))


In dit geval wordt de regel "Dit is herhaling" tien keer herhaald. En na de zin "Dit is een herhaling" volgt de inhoud van de loopcounter ``i``.

Maar wat als je niet van te voren weet hoe vaak je iets wilt herhalen? Dan gebruik je een andere soort loop, de ``while``-loop.

.. activecode:: vb-interactivity-while-loop
   :caption:
   :nocodelens:
   :language: python

   while True:
       woord = input("Typ een woord")
       lengte = len(woord)
       print ("De lengte van jouw woord is " + str(lengte))

   print ("EINDE")


N.B. Als je dit programma uitvoert, dan zal hij nooit stoppen! (Om dit te stoppen moet je de pagina herladen. Dit kan met F5.) Hij zal continu vragen om een woord in te typen en zodra je een woord intypt geeft hij de lengte van het ingetypte woord (het commando ``len()`` geeft de lengte van een woord). Dit betekent dat het woordje "EINDE" nooit geprint zal worden. Daar kunnen we echter wel een verandering in aanbrengen. We kunnen namelijk dit zeggen: Als iemand het woordje "quit" intypt, dan stoppen we met de loop. Dit stoppen doen we met het commando ``break``.

.. activecode:: vb-interactivity-while-loop-break
   :caption:
   :nocodelens:
   :language: python

   while True:
       woord = input("Typ een woord")
       if woord == "quit":
           break
       lengte = len(woord)
       print ("De lengte van jouw woord is " + str(lengte))

   print ("EINDE")


Dit worden ook wel interactieve ``while``-loops genoemd. Het aantal keren dat de loop herhaalt is dan niet van te voren bepaald, maar hangt af van de invoer van de gebruiker!
