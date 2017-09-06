Draaien
:::::::

De ``turtle`` heeft altijd een bepaalde richting. En als hij beweegt, dan beweegt hij ook die richting op. Je kunt echter de richting veranderen door het commando ``right()`` of ``left`` in te geven. Je geeft dan tussen haakjes aan hoeveel *graden* je wilt draaien.

Als je ``tina.right(90)`` ingeeft, dan draait tina 90 graden naar rechts.

.. activecode:: vb-statements-turnright
   :caption: Rechts afslaan
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.right(90)

Als je dit verandert naar ``right(180)`` ingeeft, dan draait tina zich helemaal om. Je kunt zelfs meer dan 180 graden draaien. Voer maar eens ``right(270)`` in. En met ``right(360)`` draait tina een perfect rondje. Uiteindelijk verandert ze dus dan ook niet van richting.

Als je naar rechts kan draaien, dan kun je uiteraard ook naar links draaien. Dat doe je met de functie ``left``.

.. activecode:: vb-statements-turnleft
   :caption: Links afslaan
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.left(90)

Let er wel op dat de draairichting altijd vanuit de huidige positie van de turtle wordt bepaald! Als je dus 3x achter elkaar ``right(90)`` gebruikt komt dat dus overeen met ``right(270)`` (ofwel ``left(90)``).
