try:
    def puede_votar(edad):
        if edad >= 18:
            print("puede votar")
            return edad
        else:
            print("no puedes votar")
    edad=int(input("ingrese su edad "))
    puede_votar(edad)
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")