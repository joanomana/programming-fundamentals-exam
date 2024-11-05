print("Exercise 3")

volt1 = int(input("Ingrese el primer voltaje: "))
volt2 = int(input("Ingrese el segundo voltaje: "))
volt3 = int(input("Ingrese el tercer voltaje: "))
promedio = round((volt1+volt2+volt3)/3)
if promedio < 115:
    print("VOLTAJE CORRECTO")
elif promedio > 115 and promedio < 220:
    print("ALTO VOLTAJE")
else:
    print("PELIGRO")

print(f"El promedio es: {promedio}")