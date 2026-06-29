try:
    num1=int(input("ingrese un numero"))
    for num2 in range(1,11):
        tabla=num1*num2
    print("salio el numero: ", tabla)
except ValueError: 
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
