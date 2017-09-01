Inleiding
:::::::::

Wij gaan leren tekenen met Python Turtle. Om hiermee te werken zullen we eerst een de module turtle moeten aanroepen en vervolgens een turtle-object moeten maken. Dit klinkt ingewikkeld maar kortweg willen we niet in het wilde weg opdrachten gaan roepen, maar we willen dat één specifiek schildpad opdrachten uit laten voeren. Dit doen we met de onderstaande code:

.. activecode:: vb-statements-codeturtleinstance
   :caption: Een turtle genaamd Tina
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

We krijgen nu een scherm met een schildpad met de naam ``tina`` die we vervolgens opdrachten uit kunnen laten voeren.
