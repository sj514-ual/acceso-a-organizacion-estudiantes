# 1. Creamos las dos cadenas
t1 = "Hoy he comido:"
t2 = "peras, manzanas y sopa"

# 2. Guardamos la longitud de t1 en 'cuantos' y la mostramos
cuantos = len(t1)
print(cuantos)

# 3. Capitalizamos t2 (la primera letra en mayúscula) y lo guardamos
t2 = t2.capitalize()

# 4. Guardamos el elemento de la posición 5 en 'item' y lo mostramos
# Recuerda: en Python se empieza a contar desde 0
item = t1[5]
print(item)

# 5. Concatenamos ambos con un espacio, lo guardamos en t1 y mostramos
t1 = t1 + " " + t2
print(t1)