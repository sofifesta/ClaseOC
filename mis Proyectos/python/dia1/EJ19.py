try:
    num=(7)
    num2=int(input("ingrese un numero entre 1 y 10"))
    if num2==num:
        print("acertaste")
    elif num2!=num:
        print("ese no es el numero, intenta de nuevo")
    int(input("intenta de nuevo"))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")