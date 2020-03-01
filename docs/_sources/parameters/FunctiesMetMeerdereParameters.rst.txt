Functies met meerdere parameters
::::::::::::::::::::::::::::::::

Als je een functie maakt, waar je een getal (of iets anders) aan kan meegeven, dan noem je dat een functie met een parameter. Dus de functie tekenhuis hiervoor had een parameter genaamd ``lengte``.
Hoe kun je er nou voor zorgen dat jouw functie ook meer dan één parameter kan gebruiken? Het antwoord is vrij eenvoudig: door voor de tweede een andere naam te verzinnen en dat vervolgens te gebruiken.


.. activecode:: vb-functions-kleurlijn
   :caption: Een gekleurde lijn
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   def kleurlijn(lengte, kleur):
       tina.pencolor(kleur)
       tina.forward(lengte)

   kleurlijn(10, "red")
   kleurlijn(40, "green")
