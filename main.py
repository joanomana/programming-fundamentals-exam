print("Exercise 2")

import math
a = int(input("Ingrese el lado para calcular el area de un triangulo equilatero: "))
area = ((math.sqrt(3)/4)*math.pow(a,2))
if area > 1000:
    print("DATOS NO VALIDOS")
else:
    print(f"EL AREA DEL TRIANGULO EQUILATERO ES {area}")

