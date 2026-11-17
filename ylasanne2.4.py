import math
import operator


# M - Koer

ops: dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

a, b = int(input("Sisestage esimene arv: ")), int(input("Sisestage teine arv: "))
op = input("Sisestage tehe: ")
print("auh " * ops.get(op, "auh")(a, b))


# Ülesanne 2 - Temperatuur

temp, form = input("Sisestage õuetemperatuuri formaadis <kraatid> <C (Celsius) või F (Farenheit)>: ").split()

match form:
    case "C":
        print(f"Temperatuur {temp} Farenheitides: {float(temp) * 1.8 + 32}")
    case "F":
        print(f"Temperatuur {temp} Celsiudes: {(float(temp) - 32) / 1.8}")
    case _:
        print("Valse väärtus oli sisestatud")

if form == "C":
    wind_speed = float(input("Sisestage keskmine tuule kiirus: "))
    air = float(input("Sisestage keskmine õhuniiskus: "))
    print(f"Tajutav temperatuur: {round(float(temp) + (0.33 * ((air / 100) * 6.105 * math.exp(17.27 * (float(temp) / (237.7 + float(temp)))))) - (0.7 * air - 4), 2)}")


# Ülesanne 3 - Isikukood


