Opdracht 1-2: Zigzag
::::::::::::::::::::

Hieronder staat een voorbeeldfiguur en een beginnetje van een programma. Pas de
code aan zodat tina de figuur tekent. De getallen die in de figuur staan zijn
afmetingen, deze hoef je uiteraard niet in jouw tekening erbij te zetten.

Als een geheugensteuntje staat een samenvatting van de  programmeercodes die je
tot nu toe geleerd hebt hieronder.

Als je klaar bent sla je je programma op door op ``download`` te drukken en dan
lever je dit bestand in via moodle.


2. Zigzag
---------------

.. image:: images/zigzag-100-50.png

.. activecode:: h1o2_zigzag
  :caption: Zigzag
  :nocodelens:
  :language: python
  :enabledownload:

  import turtle
  tina = turtle.Turtle()
  tina.shape("turtle")

  tina.forward(100)
  tina.left(90)


Samenvatting (1-1)
------------------

``forward(<afstand>)``
 beweeg tina <afstand> stappen naar voren
``backward(<afstand>)``
 beweeg tina <afstand> stappen naar achteren
``left(<hoek>)``
 draai tina <hoek> graden naar links
``right(<hoek>)``
 draai tina <hoek> graden naar rechts
