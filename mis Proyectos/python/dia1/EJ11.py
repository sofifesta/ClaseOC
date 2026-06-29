try:
    num1=int(input("ingresa un numero para dividir"))
    num2=int(input("ingresa otro un numero para dividir"))
    if num2 == 0:
        print("Error: No se puede dividir")
    elif num2 != 0:
        div=(num1/num2)
        print(f"la respuesta de la division entre los dos numeros es de {div}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
print("El programa continúa sin explotar.")