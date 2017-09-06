Range
:::::

Range is eigenlijk een functie die een *lijst* van getallen maakt. Zo maakt ``range(4)`` de lijst ``[0,1,2,3]``. En ``range(10)`` de lijst ``[0,1,2,3,4,5,6,7,8,9]``. Zoals je nu wel weet wordt tijdens elke herhaling de loopcounter gelijkgesteld aan het volgende getal in de lijst die range maakt. We hebben nu lijsten waarbij de getallen steeds met 0 beginnen en vervolgens met 1 toenemen. Maar stel dat je het volgende lijstje wilt hebben: ``[10,15,20,25]``. Hoe doe je dat dan? Dat doe je als volgt:

.. code-block:: python

   for i in range(10):
      tina.dot(i)
      tina.penup()
      tina.forward(i*2)
      tina.pendown()

Uitleg: ``range`` heeft dus in dit geval drie parameters. De eerste bevat de *beginwaarde*. We willen dus niet meer dat de lijst begint met 0 maar met 10. De tweede bevat de *eindwaarde*. De lijst wordt dus gevuld tot het getal 30 (*niet tot en met!!*). En als derde parameter geef je de stapgrootte mee. Die is standaard 1, maar nu hebben we hem ingesteld met 5.

.. activecode:: vb-counters-range
   :caption: range(<beginwaarde>, <eindwaarde>, <stapgrootte>)
   :nocodelens:
   :language: python

   print( range(10, 30, 5) )


Met behulp van de functie ``print`` kunnen we de lijst naar de *console* schrijven en daarmee de waarden erin bekijken.

Probeer andere waarden in te vullen voor de parameters van ``range``. N.B. Als je de lijst in omgekeerde volgorde wilt moet je niet alleen de begin en eindwaarden omdraaien maar dan is natuurlijk ook een negatieve stapgrootte nodig!
