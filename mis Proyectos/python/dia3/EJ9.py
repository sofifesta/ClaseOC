def crear_email(nombre, apellido):
    email=f"{nombre}.{apellido}@ipm.edu.ar"
    print (email)
    return email
nombre=input("ingrese su nombre ").lower()
apellido=input("ingrese su apellido ").lower()
crear_email(nombre, apellido)