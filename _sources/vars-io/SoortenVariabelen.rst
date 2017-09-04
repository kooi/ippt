Soorten variabelen
::::::::::::::::::

Bekijk eens het onderstaande programma:

.. activecode:: vb-vars-io-rekenen1
   :caption: Een rekenmachine?
   :nocodelens:
   :language: python

   getal1 = input("Geef een getal")
   getal2 = input("Geef nog een getal")
   som = getal1 + getal2
   print ("De som van getal1 en getal2 is")
   print (som)


Je zou denken dat je hiermee een optelprogramma hebt gemaakt, maar dat valt vies tegen! Probeer maar eens een paar getallen op te tellen en kijk goed naar het resultaat.

Wat gaat hier nou mis? Als je voor het eerste getal 22 kiest en voor het tweede getal 56, dan is het resultaat 2256. Wat is hier misgegaan?

Python heeft de twee 'getallen' aan elkaar vastgeplakt. Dit doet hij, omdat hij denkt dat je twee stukjes tekst aan elkaar wilt vastplakken. Net alsof je "programmeren is" en "fun" aan elkaar wilt vastplakken. Maar wij willen niet dat Python die twee getallen aan elkaar vastplakt, maar dat ze bij elkaar worden opgeteld! Eigenlijk willen we dat Python de twee getallen ook *echt* als twee getallen gaat beschouwen. De vraag is: Hoe doen we dat?

De input-functie is hier van belang. Die zegt eigenlijk altijd dat de invoer van de gebruiker als tekst moet worden beschouwd. Wij kunnen expliciet aangeven dat de invoer toch moet worden opgevat als een echt getal. Dit doen we door de functie ``int()`` te gebruiken. Dit ziet er als volgt uit:

.. activecode:: vb-vars-io-rekenen2
   :caption: Een rekenmachine!
   :nocodelens:
   :language: python

   getal1 = int(input("Geef een getal"))
   getal2 = int(input("Geef nog een getal"))
   som = getal1 + getal2
   print ("De som van getal1 en getal2 is")
   print (som)


Let vooral op het gebruik van de functie ``int()``! int is een afkorting voor integer. Het is de engelstalige benaming voor een geheel getal. Je zegt hier eigenlijk: Hetgeen dat de gebruiker invoert met de input functie moet worden opgevat als een getal.
