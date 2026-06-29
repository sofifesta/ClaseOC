try:  
    def minutos_horas(minutos):
        horas=minutos//60
        min=minutos%60
        print(f"son {horas} horas con {min} minutos")
        return horas
    minutos=int(input("ingrese un tiempo en minutos"))
    minutos_horas(minutos)
except ValueError:
    # Esto se ejecuta si el usuario escribe texto
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
    
except ZeroDivisionError:
    # Esto se ejecuta si escribe 0
    print("❌ Error: No se puede dividir por cero.")
    
print("El programa continúa sin explotar.")