Interactieve programma's met de input() functie
:::::::::::::::::::::::::::::::::::::::::::::::

Met de print functie kun je gegevens op het scherm printen. Maar wat als je nou wilt dat de gebruiker iets kan invoeren? Heb je daar ook iets voor? Zie bijvoorbeeld het volgende programma. Het tekent een vierkant op basis van het antwoord van de gebruiker.

.. activecode:: vb-vars-io-inputkleur
   :caption: Vragen om een kleurtje
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   kleur = input("Kies een kleur (wel Engels):")
   tina.pencolor(kleur)
   for i in range(4):
       tina.forward(20)
       tina.right(90)
