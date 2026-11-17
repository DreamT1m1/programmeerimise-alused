from datetime import *
from math import pi


#1
today = date.today()
print(f"Today is {today.strftime("%m month, %Y year and %d day")}")
print(f"It's {30 - today.day} days til the end of the month, ~{(12 - today.month) * 30 + (30 - today.day)} days til year's end")

birthday = date(2002, 5, 8)
print(f"I was born on {birthday.strftime("%d.%m.%Y")}")
difference = today - birthday
print(f"So now I am {difference.days // 365} years,  {difference.days % 365 // 30} months, {difference.days % 365 % 30} days old")

#2
"""
Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
+Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
+Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

Sulud mõjutavad seda, mis järjekorras tehteid tehakse, ehk annab prioriteedi
"""
print("Trying to solve 3 + 8 / (4 - 2) * 4")
print(f"First: {3 + 8 / (4 - 2) * 4}")
print(f"Second: {3 + (8 / 4) - 2 * 4}")
print(f"Third: {(3 + 8) / 4 - 2 * 4}")
print("Etc")

#3
r = float(input("Enter circle's radius: "))
square_side = round(r * 2, 2)
print(f"Square surface: {round(square_side ** 2, 2)}")
print(f"Square perimeter: {square_side * 4}")
print(f"Circle surface: {round(pi * r ** 2, 2)}")

#4
EARTH_RADIUS = 6378000 # m
circumference = round(2 * pi * EARTH_RADIUS, 2)
TWO_EURO_COIN_RADIUS = 0.02565 # m
print(f"We will need ~{circumference // TWO_EURO_COIN_RADIUS} coins")

#5
print("kill-koll kill-koll killadi-koll " * 2, "kill-koll " * 4)

#6
song = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.



....Sisend, väljund, tingimus....
"""
print(song.upper())

#7
a, b = float(input("Sisesta ristküliku ühe poole mõõt: ")), float(input("Ja sisesta selle lähiskülje mõõt: "))
print(f"Perimeter: {2 * (a + b)}")
print(f"Area: {a * b}")

#8
fuel_tanked = float(input("Enter tanked fuel amount in liters: "))
driven_km = float(input("Enter driven km's amount: "))
print(f"Fuel expense per 100 km: {fuel_tanked / driven_km * 100}")

#9
SPEED = 29.9 # km/h
t = float(input("Enter amount of minutes: "))
print(f"If speed is {SPEED}, then answer is: {round(SPEED * (t / 60), 2)}")

#10
minutes = float(input("Enter amount of minutes: "))
print(f"{minutes // 60}:{minutes % 60}")
