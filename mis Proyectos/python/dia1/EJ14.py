try:
    nota= int(input("ingrese su nota: "))
    if nota >= 6:
        print("uff aprobaste")
    elif nota<6:
        print("mal ahi nos vemos en el cumple de barry")
    else:
        print("ERROR")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.") 