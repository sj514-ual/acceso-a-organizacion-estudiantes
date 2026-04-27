# Leemos la lista separada por comas
entrada = input()
# La convertimos en una lista de números de verdad
lista = [int(x) for x in entrada.split(',')]

# Ordenamos la lista como pide el profe
lista.sort()

# Creamos la lista sin repetidos
listaSinDuplicados = []
for n in lista:
    if n not in listaSinDuplicados:
        listaSinDuplicados.append(n)

# Mostramos el resultado final
print(listaSinDuplicados)