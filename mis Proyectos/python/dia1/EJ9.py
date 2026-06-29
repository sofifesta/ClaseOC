try:
    dias=int(input("ingrese una cantidad de dias por favor"))
    seg=(dias*24*60*60)
    print(f"la cantidad de dias pasado a segundos es {seg}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")