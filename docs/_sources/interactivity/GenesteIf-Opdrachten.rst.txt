Geneste if-opdrachten
:::::::::::::::::::::

Je kunt ook ``if``-opdrachten in ``if``-opdrachten plaatsen. Dit worden *geneste* ``if``-opdrachten genoemd.

.. activecode:: vb-interactiviteit-geneste-if
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


Als ``num`` groter is dan 0, dan komt het programma in een tweede ``if``. Deze tweede ``if`` wordt alleen uitgevoerd als de vergelijking ``num >= 0`` waar is. De eerste ``else`` die er staat hoort bij de tweede ``if``. Dit kun je zien aan de hand van de tabjes die zijn gebruikt. Het goed gebruiken van de tabs is hier dus ontzettend belangrijk!

Je kunt ook ``if``-opdrachten in ``if``-opdrachten in ``if``-opdrachten plaatsen. In principe kun je ``if``-opdrachten oneindig gaan nesten. Maar in de praktijk hangt het af van hoe slim je het programmeert en hoe moeilijk de keuzestructuur is.
