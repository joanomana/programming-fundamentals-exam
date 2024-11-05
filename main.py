print("Exercise 1")
volt1 = int(input("Enter the voltage: "))
volt2 = int(input("Enter the voltage: "))
volt3 = int(input("Enter the voltage: "))
volt4 = int(input("Enter the voltage: "))
volt5 = int(input("Enter the voltage: "))
promedium = round((volt1 + volt2 + volt3 + volt4 + volt5) / 5)
if promedium > 220: 
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
