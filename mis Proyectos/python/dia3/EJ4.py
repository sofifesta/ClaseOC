try:
    def comparar_nums(a, b, c):
        if a > b and a > c:
            return a
            print("a es mayor que b y c")
        elif b > c and b > c:
            return b
            print("b es mayor que a y c")
        else:
            return c
            print("c es mayor que a y b")
    a = int(input("ingrese un numero "))
    b = int(input("ingrese un numero "))
    c = int(input("ingrese un numero "))
    print(comparar_nums(a,b,c))
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")