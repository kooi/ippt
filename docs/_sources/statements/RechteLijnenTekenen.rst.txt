Rechte lijnen tekenen
:::::::::::::::::::::

Nu we een turtle hebben (met de naam ``tina``). Met de opdracht ``forward(100)``, gaat de turtle 100 stappen vooruit. Om aan te geven welke ``turtle`` het commando op moet volgen moeten we in dit geval zeggen ``tina.forward()``. (We hebben *nog* maar één turtle maar in de toekomst zouden we er natuurlijk wel meerdere kunnen hebben.)

.. activecode:: vb-statements-forward
   :caption: 100 stappen vooruit
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.forward(100)

Analoog hieraan kunnen we ook het commando ``backward(100)`` gebruiken voor Tina (``tina.backward(100)``) en dan gaat Tina 100 stappen achteruit.

.. activecode:: vb-statements-backward
   :caption: 100 stappen achteruit
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.backward(100)
