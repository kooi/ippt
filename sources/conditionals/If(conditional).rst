if
::

Vaak wil je een opdracht pas uitvoeren als is voldaan aan een bepaalde voorwaarde. Pas als de voorwaarde klopt, dan moet de opdracht uitgevoerd worden. Dit kun je realiseren door de ``if``-opdracht te gebruiken. Zie eens het volgende voorbeeld:

.. code-block:: python

   if 3 < 4:
       print ("Hoi")

Na de ``if`` volgt een vergelijking. Een vergelijking is altijd waar (``True``) of onwaar (``False``). Als de vergelijking waar is, dan worden de opdrachten die bij de ``if`` horen uitgevoerd. Alle opdrachten die zijn ingesprongen na de ``if`` horen bij die if. Nog een voorbeeld dat dit illustreert:

.. activecode:: vb-conditionals-if
   :caption: de vergelijking is in dit geval waar omdat 3 kleiner is dan 4
   :nocodelens:
   :language: python

   if 3 < 4:
       print ("Hoi")
       print ("Dit hoort ook bij de if")

   print ("Dit hoort niet meer bij de if")


Zoals gezegd is ``3 < 4`` een wiskundige vergelijking waarmee je ongetwijfeld bekend bent. De bovenstaande code voert nu alle drie de ``print``-opdrachten uit. Maar wat zou er gebeuren als je i.p.v. ``3 < 4`` de vergelijking ``3 > 4`` zou schrijven? Dan zou alleen de laatste print-opdracht uitgevoerd worden! Probeer het eens.

Je kunt de ``if``-opdracht ook uitbreiden met een ``else``. Als de vergelijking na de ``if`` onwaar is, dan zal de ``else``-tak uitgevoerd worden. Zie maar eens het volgende programma:

.. activecode:: vb-conditionals-if2
   :caption: doei
   :nocodelens:
   :language: python

   if 4 < 3:
       print ("hoi")
   else:
       print ("doei")


In het bovenstaande voorbeeld wordt alleen de ``else``-tak uitgevoerd. Dit, omdat de vergelijking na de ``if`` onwaar is. Draai de vergelijking om door ook bij deze de ``<`` te veranderen in een ``>``.
