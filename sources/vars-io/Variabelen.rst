Variabelen
::::::::::

Vaak wil je in je programma tijdelijk gegevens bewaren. Dit doe je met variabelen. Een variabele kun je zien als een emmer met een label erop. Je kunt er iets in zetten en je kunt er iets uithalen. Hieronder zie je een stukje code en een plaatje waarop te zien is wat er gebeurt:

.. code-block:: python

   a = 20
   b = 15
   c = "hallo"

.. image:: images/vars1.png

Je ziet dus dat er nu drie emmers zijn. Elke emmer heeft een naam en een inhoud. In het begin zijn alle emmers leeg. Maar na de drie regels van hierboven verandert de zaak:
In de emmer met als naam ``a`` komt namelijk het getal 20 te staan. In emmer ``b`` komt 15 te staan. En in c komt de tekst ``"hallo"`` te staan.

We kunnen nu ook een vierde emmer genaamd d in het leven roepen. In die variabele kunnen we het verschil tussen a en b plaatsen. Dat gaat zo:

.. code-block:: python

   a = 20
   b = 15
   c = "hallo"

   d = a - b

.. image:: images/vars2.png


We halen dus het getal 20 uit emmer ``a`` en we halen het getal 15 uit emmer ``b``. Het verschil wordt vervolgens berekend en het antwoord komt in emmer ``d`` te staan.

.. activecode:: vb-vars-io-
   :caption: Rekenen met variablen
   :nocodelens:
   :language: python

   a = 20
   b = 15
   c = "hallo"

   d = a - b

   print (a)
   print (b)
   print (c)
   print (d)


En we kunnen de variabelen ook weer gebruiken om bijvoorbeeld de turtle vooruit te laten bewegen. In plaats van dat je een getal meegeeft aan de forward functie, kun je bijvoorbeeld ook een variabelenaam meegeven. En ook een berekening met een variabele! Dat ziet er dan zo uit: ``forward(d*10)``
