try:
    num1= int(input("ingresa un numero"))
    if num1<0:
        print("el numero elegido es negativo")
    elif num1>0:
        print("el numero elegido es positivo")
    else:
        print("el numero elegido es 0 ") 
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")