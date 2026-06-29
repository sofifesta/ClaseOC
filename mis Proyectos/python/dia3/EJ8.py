try:
    def calcular_precio_final(precio,descuento):
        precio2=precio-precio*descuento/100
    
        return precio2
    precio=int(input("ingrese el precio original "))
    descuento=int(input("ingrese el descuento "))
    print(calcular_precio_final(precio,descuento))
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")