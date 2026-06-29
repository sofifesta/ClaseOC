try:
    def multiplicar_pantalla(a):
        resultado = a*a
        return resultado
    a=int(input("elegi un numero "))
    print(multiplicar_pantalla(a))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")    
print("El programa continúa sin explotar.")
