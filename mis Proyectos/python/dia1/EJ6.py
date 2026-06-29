try:
    num1=int(input("ingrese su nota del uno al diez"))
    num2=int(input("ingrese su nota del uno al diez"))
    num3=int(input("ingrese su nota del uno al diez"))
    prom=((num1+num2+num3)/3)
    print(f"el promedio de tus notas es{prom}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("El programa continúa sin explotar.")
