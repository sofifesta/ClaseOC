try:
    celcius=int(input("ingrese una cantidad de grados razonable para la unidad de celsius "))
    faren=((celcius*9/5)+32)
    print(f"la cantidad de grados celcius expresada en fahrenheit es {faren}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")