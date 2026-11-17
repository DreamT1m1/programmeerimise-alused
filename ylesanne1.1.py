# YLESANNE 1.1
import random
from math import pi

#1
print(f"Tere, maailm! Tervitan sind {input('Sisestage enda nimi: ')}! Sa oled {input('Sisestage oma vanus: ')} aastat vana.")

#2
"""
Mis tüüpi on järgnevad muutujad:

a) vanus = 18. Vastus: int
b) eesnimi = "Jaak". Vastus: str
c) pikkus = 16.5. Vastus: float
d) kas_käib_koolis = True. Vastus bool
Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
Kirjuta kood tüüpide kontrollimiseks. Vastus: näiteks isinstance() funktsioon
"""

print(isinstance(True, bool))
print(isinstance("lol", bool))

#3
candies_count = random.randint(0, 30)
print(f"Laual on {candies_count} komme")
candies_to_take = int(input("Palju komme soovite laualt võtta: "))
candies_count -= candies_to_take
print(f"Nüüd on laual {candies_count}")

#4
perimeter = int(input("Sisestage palun puu ümbermõõt: "))
d = perimeter / pi
print(f"Puu läbimõõt: {d}")

#5
