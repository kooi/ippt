elif
::::

Met de ``if``-``else`` opdracht kun je eigenlijk een onderscheid maken tussen twee verschillende mogelijkheden: of de ``if``-voorwaarde is waar of hij is onwaar. Soms zijn er meer dan twee mogelijkheden en hebben we meer dan twee takken nodig. Een manier om een dergelijke berekening vorm te geven is een *gekoppelde voorwaarde*:

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
