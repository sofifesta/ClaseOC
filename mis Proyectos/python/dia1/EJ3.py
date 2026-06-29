num=int(input("ingrese un monto y te diremos si es par o impar"))
resto=(num%2)
if resto == 0:
    print("el numero ingresado anteriormente es un numero llamado par")
elif resto > 0:
    print("el numero ingresado anteriormente es un numero llamado impar")
