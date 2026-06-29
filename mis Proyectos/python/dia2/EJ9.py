precios= {
    "manzana": 100,
    "banana": 50,
    "naranja": 80,
}
fruta=input("que fruta queres ")
kg=int(input("cuantos kg queres "))
if fruta=="manzana":
    precio=kg*100
elif fruta=="banana":
    precio=kg*50
else:
    precio=kg*80
print("te vas a costar: ", precio)