import math

# El programa te pedirá tres números (los tres lados)
a = float(input())
b = float(input())
c = float(input())

# 1. Comprobamos si los datos son positivos
if a <= 0 or b <= 0 or c <= 0:
    print("Error en los datos de entrada")
# 2. Comprobamos si los lados pueden formar un triángulo
elif not (a < (b + c) and b < (a + c) and c < (a + b)):
    print("No es un triángulo")
else:
    # Calculamos el semiperímetro (s)
    s = (a + b + c) / 2
    # Aplicamos la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Mostramos el resultado con 2 decimales
    print(f"Área = {area:.2f}")