try:
    def area_circulo(radio):
        area = 3.1416*radio*radio
        return area
    radio=int(input("elegi el radio del circulo "))
    print (area_circulo(radio))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")

print("El programa continúa sin explotar.")