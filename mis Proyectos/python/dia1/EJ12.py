try:
    num1= int(input("ingresa un numero"))
    num2= int(input("ingresa un numero"))
    if num1>num2:
        print(f"el numero {num1} es mayor que el numero {num2}")
    elif num2>num1:
        print(f"el numero {num2} es mayor que el numero {num1}")
except  ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")