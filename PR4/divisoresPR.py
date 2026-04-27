# Creamos una lista vacía para guardar los números que cumplan la condición
resultados = []

# Recorremos los números desde 2000 hasta 3200 (ponemos 3201 para que incluya el 3200)
for i in range(2000, 3201):
    # Si es divisible por 7 (resto 0) y NO es divisible por 5 (resto distinto de 0)
    if i % 7 == 0 and i % 5 != 0:
        resultados.append(str(i))

# Los unimos todos con una coma y los imprimimos en una sola línea
print(",".join(resultados))