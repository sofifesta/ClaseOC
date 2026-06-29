contexplotion=0
norma = int(input("ingrese un numero 0 o 1 "))
if norma==0:
    print("Norma a: 'Verde/blanco, Verde, Amarillo/blanco, Azul, Azul/blanco, Amarillo, Marron/blanco y Marron'")
elif norma==1:
    print("Norma b:'Amarillo/blanco, Amarillo, Verde/blanco, Azul, Azul/blanco, Verde, Marron/blanco y Marron'")
else:
    print("No se ha ubicado en los sistemas esa variable")
print("ahora vamos a ver cuantas normas ha explotado")
print("empezare a contar en:")
print("1...")
print("2...")
print("3...")
if norma==1:
    cable1=int(input("en que posicion se encuentra el cable verde/blanco en norma a "))
    if cable1 == 1:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
    cable2=int(input("en que posicion se encuentra el cable verde en norma a "))
    if cable2 == 2:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
    cable3=int(input("en que posicion se encuentra el cable azul en norma a "))
    if cable3 == 4:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
else:
    cable1=int(input("en que posicion se encuentra el cable verde/blanco en norma b "))
    if cable1 == 3:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
    cable2=int(input("en que posicion se encuentra el cable verde en norma a "))
    if cable2 == 6:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
    cable3=int(input("en que posicion se encuentra el cable azul en norma a "))
    if cable3 == 4:
        print("respuesta correcta")
    else:
        print("explotaste la ficha")
        contexplotion=contexplotion+1
print("explotaste la ficha: ", contexplotion)
ficha=1000
costo=contexplotion*1000
print("le debes a Vaccalluzzo:", costo,"dolares")
print("Vaccalluzzo acepta Mercado Pago, Efectivo o Multiple choice")
print("ahora vamos a ver cual es tu nota")
print("vamos a realizar 10 fichas")
print("si haces bien 6 o mas aprobas")
print("sino a Diciembre")
contnota=0
ficha1=input("cual es el codigo EXACTO de la norma a")
if ficha1==T568A
    print("correcto")
    contnota=contnota+1
else:
    print("linea 67")
    print("mal no sabes") 
ficha2=input("cual es el codigo EXACTO de la norma b")
      