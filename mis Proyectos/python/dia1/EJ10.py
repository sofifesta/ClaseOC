try:
    pre_ori=int(input("ingrese el precio original"))
    porcentaje=int(input("ingrese el porcentaje de descuento"))
    desc= ((pre_ori*porcentaje)/100)
    pre_final= (pre_ori-desc)
    print(f"el descuento registrado es de {desc} y el precio final es de {pre_final}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
print("No exploto")
