import math

datos = []
# Bucle para leer datos hasta encontrar -99
while True:
    t = float(input())
    if t == -99:
        break
    # Solo guardamos si está en el rango [-50, 50]
    if -50 <= t <= 50:
        datos.append(t)

n = len(datos)

if n == 0:
    media = None
    de = None
    print("Ningún dato válido")
else:
    media = sum(datos) / n
    # Calculamos la desviación estándar (de)
    suma_cuadrados = sum(ti**2 for ti in datos)
    de = math.sqrt((suma_cuadrados / n) - (media**2))
    
    print(f"Nº de datos válidos: {n}")
    print(f"Tmedia= {media:.2f}")
    print(f"σ = {de:.2f}")