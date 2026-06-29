clave1= ("profesor.malvado.mancini")
clave2 = int(input("ingrese una contraseña y le dire si es correcta: " ))
if clave1 == clave2:
    print("acceso permitido")
elif clave1 != clave2:
    print("acceso denegado")