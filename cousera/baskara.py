import math

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é:", raiz1)
else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A raiz da equação são:", raiz1, "e", raiz2)
