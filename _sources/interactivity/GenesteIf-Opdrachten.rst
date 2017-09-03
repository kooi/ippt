elif
::::

Geneste if-opdrachten

Je kunt ook if-opdrachten in if-opdrachten plaatsen. Dit worden geneste if-opdrachten genoemd.

.. activecode:: vb-interactiviteit-
   :caption:
   :nocodelens:
   :language: python

num = float(input("Geef een getal "))

if num >= 0:
    if num == 0:
        print("Je hebt het getal 0 ingevoerd")
    else:
        print("Je hebt een positief getal ingevoerd!")
else:
    print("Je hebt een negatief getal ingevoerd!")


Als num groter is dan 0, dan komt het programma in een tweede if. Deze tweede if wordt alleen uitgevoerd als de vergelijking num >= 0 waar is. De eerste else die er staat hoort bij de tweede if. Dit kun je zien aan de hand van de tabjes die zijn gebruikt. Het goed gebruiken van de tabs is hier dus ontzettend belangrijk!

Je kunt ook if-opdrachten in if-opdrachten in if-opdrachten plaatsen. In principe kun je if-opdrachten oneindig gaan nesten. Maar in de praktijk hangt het af van hoe slim je het programmeert en hoe moeilijk de keuzestructuur is.



.. activecode:: vb-conditionals-gekoppelde-voorwaarde1
   :caption: Gekoppelde voorwaarde 1
   :nocodelens:
   :language: python

   x = int(input("x"))
   y = int(input("y"))

   if x < y:
       print ("x is kleiner dan y")
   elif x > y:
       print ("x is groter dan y")
   else:
       print ("x en y zijn gelijk")


``elif`` is een afkorting van ``else if``. Ook hier wordt precies één tak uitgevoerd. Er is geen limiet op het aantal ``elif`` instructies. Staat er een ``else`` opdracht, dan is dat het einde, maar deze hoeft er niet te staan.

.. activecode:: vb-conditionals-gekoppelde-voorwaarde2
   :caption: Gekoppelde voorwaarde 2
   :nocodelens:
   :language: python

choice = input("Kies een letter (a,b,c)")
if choice == "a":
      print("je hebt gekozen voor a")
elif choice == "b":
      print("je hebt gekozen voor b")
elif choice == "c":
      print("je hebt gekozen voor c")
else:
	print ("Je hebt voor een andere letter gekozen")


Elke voorwaarde wordt op volgorde gecontroleerd. Is de eerste onwaar, dan wordt de volgende gecontroleerd, enzovoorts. Is er één waar dan wordt de bijbehorende tak uitgevoerd en de instructie eindigt. Zelfs als er meer dan één voorwaarde waar zou zijn. Alleen de tak bij de eerste keer waar wordt uitgevoerd.
Dit alles wordt ook uitgelegd in het volgende filmpje: https://www.youtube.com/watch?v=2WYpO5yZBuA (en dit voorbeeld is gebruikt: https://trinket.io/python/30d3c020bd)
