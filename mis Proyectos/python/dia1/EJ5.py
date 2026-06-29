try:
    b=int(input("ingrese la base de un rectangulo"))
    h=int(input("ingrese la altura de un rectangulo"))
    area= (b*h)
    print(f"el area del rectangulo es {area}cm")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")