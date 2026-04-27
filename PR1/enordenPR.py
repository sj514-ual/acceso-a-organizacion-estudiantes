# Pedimos los 3 números al usuario
n1 = float(input())
n2 = float(input())
n3 = float(input())

# Comprobamos si están en orden creciente
# Esto devolverá True si n1 <= n2 <= n3, y False si no
en_orden = (n1 <= n2) and (n2 <= n3)

# Imprimimos solo el valor lógico como pide el profe
print(en_orden)