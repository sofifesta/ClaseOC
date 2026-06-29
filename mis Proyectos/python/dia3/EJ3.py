try:
    def resto_numero(a):
        if a%2==0:
            return True
            print("es par")
        else:
            return False
            print("es impar")
    a=int(input("elegi un numero "))
    print(resto_numero(a))
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")