# Pedimos la altura al usuario
altura = int(input())

# Usamos un bucle para cada fila
for i in range(1, altura + 1):
    fila = []
    # Generamos los números impares desde (2*i - 1) hasta 1
    for j in range(2*i - 1, 0, -2):
        fila.append(str(j))
    
    # Unimos los números con un espacio y los mostramos
    print(" ".join(fila))