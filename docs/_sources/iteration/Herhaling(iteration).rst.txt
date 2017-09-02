Herhaling (iteration)
:::::::::::::::::::::

Als je een vierkant wilt gaan tekenen met zijden van 100 pixels, dan zou je het volgende programma kunnen uitvoeren:

.. activecode:: vb-iteration-square
   :caption: Een vierkant met zijde 100
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   tina.forward(100)
   tina.right(90)
   tina.forward(100)
   tina.right(90)
   tina.forward(100)
   tina.right(90)
   tina.forward(100)
   tina.right(90)


Merk op dat de twee commando's ``forward(100)`` en ``right(90)`` vier keer worden herhaald! Zou het niet veel beter zijn als je de computer kort en krachtig kan aangeven dat hij die twee commando's vier keer moet uitvoeren, i.p.v. dat je de twee commando's vier keer moet gaan opschrijven? Dat kan! En hiervoor maak je gebruik van de herhaalinstructie (wordt ook een loop genoemd). Het bovenstaande programma kan dus ook als volgt worden geschreven:

.. activecode:: vb-iteration-square2
   :caption: Een vierkant met zijde 100 *met herhaling*
   :nocodelens:
   :language: python

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")

   for i in range(4):
       tina.forward(100)
       tina.right(90)


De for-opdracht zorgt ervoor dat de twee opdrachten eronder vier keer worden uitgevoerd. Als er ``for i in range (14)`` zou staan bijvoorbeeld, dan zouden die twee opdrachten 14 keer worden herhaald. Let wel op dat je eerst een *tab* plaatst voor de opdrachten die herhaald moeten worden. Dit noem je inspringen. Hetgeen dat herhaald moet worden, dient dus te worden ingesprongen. Als je dat niet doet, dan krijg je een foutmelding.
