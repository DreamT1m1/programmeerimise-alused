import math


#Esialgses failis oli palju koodistiili ja süntaksise vigu

print("Ruudu karakteristikud")
a = input('Sisesta ruudu külje pikkus => ')

if a.isdigit():
    a = int(a)
    s = a ** 2
    print("Ruudu pindala", s)
    p = 4 * a
    print("Ruudu ümbermõõt", p)
    di = a * math.sqrt(2)
    print("Ruudu diagonaal", round(di, 2))
    print()

print("Ristküliku karakteristikud")
b = input("Sisesta ristküliku 1. külje pikkus => ")
c = input("Sisesta ristküliku 2. külje pikkus => ")

if b.isdigit() and c.isdigit():
    b, c = int(b), int(c)
    s = b * c
    print("Ristküliku pindala", s)
    p = 2 * (b + c)
    print("Ristküliku ümbermõõt", p)
    di = math.sqrt(b * 2 + c * 2)
    print("Ristküliku diagonaal", round(di))
    print()

print("Ringi karakteristikud")
r = input("Sisesta ringi raadiusi pikkus = > ")

if r.isdigit():
    r = int(r)
    d = 2 * r
    print("Ringi läbimõõt", d)
    s = math.pi * r ** 2
    print("Ringi pindala", round(s, 2))
    c = 2 * math.pi * r
    print("Ringjoone pikkus", round(c, 2))
