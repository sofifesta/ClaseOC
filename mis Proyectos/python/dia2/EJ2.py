try:
    notas=[8, 9, 7, 10, 6]
    for num in notas:
        prom=sum(notas)/5
    print(f"el promedio es {prom}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
