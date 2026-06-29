try:
    hs=int(input("ingrese la cantidad de horas que laburas "))
    pago=int(input("ingrese la cantidad de plata que ganas por hora"))
    sal= (hs*pago)
    print(f"tu salario será de {sal}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")
print("El programa continúa sin explotar.")
