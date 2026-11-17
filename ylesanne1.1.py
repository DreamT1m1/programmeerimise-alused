# YLESANNE 1.1
import random
from math import pi, sqrt

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
n = int(input("Sisestage ristküliku üks mõõde: "))
m = int(input("Sisestage teine mõõde: "))
print(f"Ristküliku diagonaal: {round(sqrt(n ** 2 + m ++ 2), 2)}")

#6
"""
Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")

Peaks olema teepikkus / aeg
"""

#7
print("Sisestage 5 täisarvu")
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input()),
print(f"Aritmeetiline keskmine: {round((a + b + c + d + e) / 5, 2)}")


#8
print("  @..@\n (----)\n(\\__/)\n^^ "" ^^")

#9
print("Sisestage kolmnurga kolme serva mõõdud")
a, b, c = int(input()), int(input()), int(input())
p = a + b + c
print(f"Kolmnurga ümbermõõt {p}")

#10
PRICE = 12.9
people_count = int(input("Sisestage mitme inimese peale võtate pitsat: "))
tips = 12.9 * 0.1
print(f"Jätsite {round(tips, 2)} jootraha. Igaüks peab maksma: {round((PRICE - tips) / people_count, 2)}")

#11
try:
    some_int = int(input("Sisestage mingi täisarv: "))
except ValueError:
    print("Sisestasite vale väärtuse!")
