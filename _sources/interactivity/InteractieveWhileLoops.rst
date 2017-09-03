Nog een keer loops, maar dan interactieve while loops
:::::::::::::::::::::::

In één van de vorige lesbrieven heb je geleerd hoe loops werken. Als je wilt dat iets tien keer wordt herhaald, dan gebruik je de for-loop. Hier een voorbeeld:

for i in range(10):
	print ("Dit is herhaling " + str(i))

In dit geval wordt de regel "Dit is herhaling" tien keer herhaald. En na de zin Dit is een herhaling volgt de inhoud van de loopcounter i. De uitvoer van dit programma kun je zien op: https://trinket.io/python/cb7ab7c8af

Maar wat als je niet van te voren weet hoe vaak je iets wilt herhalen? Dan gebruik je een andere soort loop. De while-loop. Zie hier het onderstaande programma (of klik hier: https://trinket.io/python/63a74aa944):

while True:
  woord = input("Typ een woord")
  lengte = len(woord)
  print ("De lengte van jouw woord is " + str(lengte))

print ("EINDE")

Als je dit programma uitvoert, dan zal hij nooit stoppen. Hij zal continu vragen om een woord in te typen en zodra je een woord intypt geeft hij de lengte van het ingetypte woord. Dit betekent dat het woordje EINDE nooit geprint zal worden. Daar kunnen we echter wel een verandering in aanbrengen. We kunnen namelijk dit zeggen: Als iemand het woordje quit intypt, dan stoppen we met de loop. Dit stoppen doen we met het commando break. Dit ziet er als volgt uit: (https://trinket.io/python/33a10169a5):

while True:
  woord = input("Typ een woord")
  if woord == "quit":
    break

  lengte = len(woord)
  print ("De lengte van jouw woord is " + str(lengte))

print ("EINDE")

Dit worden ook wel interactieve while loops genoemd. Het aantal keren dat de loop herhaalt is dan niet van te voren bepaald, maar hangt af van de invoer van de gebruiker!
