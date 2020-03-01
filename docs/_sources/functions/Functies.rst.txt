Functies
::::::::

We gaan in aan de slag met *functies*. Wat een functie is zal ik uitleggen door een voorbeeld te geven:

Met het onderstaande programma zorg je ervoor dat de turtle een huis tekent.

.. activecode:: vb-functions-huis
   :caption: Een huis
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

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


Het zou toch echt makkelijker zijn als je de computer in een keer had kunnen zeggen dat de turtle een huis had moeten tekenen. Wat zou het handig zijn als je een opdracht zoiets als ``tekenhuis()`` had kunnen invoeren die dan direct voor jou het huis tekent. Eerder heb ik gezegd dat dat niet kan, want je moet de computer altijd in kleine stapjes vertellen wat hij moet doen. Maar eigenlijk klopt dat niet helemaal. Het kan namelijk wel! Maar dan moet je wel zelf aan het begin zeggen wat ``tekenhuis()`` dan moet doen. We noemen dit een *functie* en je hoeft dus maar een keer aan te geven wat die functie moet doen. Later kun je meerdere malen gebruik maken van deze functie door slechts de naam van de functie op te schrijven.

We gaan eerst een functie ``tekenhuis()`` maken:

.. activecode:: vb-functions-tekenhuis
   :caption: tekenhuis()
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

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


Merk op dat je bij het maken van zo'n functie met de afkorting ``def`` begint. ``def`` staat voor definiëer. Dus je definiëert een functie genaamd ``tekenhuis``. De haakjes erachter horen er altijd bij. En wat ook heel belangrijk is, is dat alle opdrachten die bij de functie horen moeten worden ingesprongen (dus een tab ervoor).

Nu heb je dus eigenlijk je eigen commando/functie gemaakt. Deze functie kun je zo vaak aanroepen als je wilt.

Probeer maar eens het programma uit.

.. activecode:: vb-functions-tekenhuis2
   :caption: 2x tekenen met tekenhuis()
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

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

   tekenhuis()
   tekenhuis()


Let vooral op de laatste twee regels. Door de opdracht ``tekenhuis()`` twee keer te geven, worden er twee huizen getekend. De huizen worden nog wel op dezelfde plek getekend, waardoor je aan het eind maar één huis ziet. Dit kunnen we oplossen door na het eerste huisje de turtle te verplaatsen, zodat het tweede huisje ernaast wordt getekend. Je kunt tussen de twee ``tekenhuis()`` commando's dus bijvoorbeeld

.. code-block:: python

   tina.penup()
   tina.forward(50)
   tina.pendown()


invoegen. De huizen komen zo naast elkaar te staan.
