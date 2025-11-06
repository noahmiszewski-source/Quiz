# del 1 - Hälsning

namn = input("vad heter du? ")
print("Hej", namn)

# del 2 - Slumpa ett tal

from random import randint

tal = randint(1, 10)
Gissning = int(input("Gissa ett tal mellan 1 till 10: "))
if Gissning == tal:
	print("Rätt gissat!")
else:
	print("Fel gissat, talet var", tal)

