try:
    dol=int(input("ingrese un monto de dolares"))
    num= (dol*1436)
    print(f"la cantidad de dolares convertido a pesos son {num}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")

