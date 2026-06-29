pal=input("Escribi una palabra ")
cont=0
for letras in pal:
    if letras in "aeiouAEIOU":
        print("salio una vocal")
        cont=cont+1
print("salieron: ", cont ,"vocales")
