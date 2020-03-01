Opdracht 3-1: Veel sterren
::::::::::::::::::::::::::

Opdracht
--------

Teken het onderstaande plaatje na. Zorg ervoor dat je niet zelf de ster gaat
tekenen maar teken de ster m.b.v. de functie ``tekenster()``.

.. image:: images/sterren.png

.. activecode:: h3o1_veel-sterren
   :caption: 3x een ster tekenen
   :nocodelens:
   :language: python
   :enabledownload:

   import turtle
   tina = turtle.Turtle()
   tina.shape("turtle")
   tina.speed(10)

   def tekenster ():
       for i in range(12):
           tina.forward(50)
           tina.backward(50)
           tina.right(30)
