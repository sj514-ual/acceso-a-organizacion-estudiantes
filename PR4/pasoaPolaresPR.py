import math

# Pedimos las coordenadas al usuario
x = float(input())
y = float(input())

# Calculamos el radio r
r = math.sqrt(x**2 + y**2)

# Calculamos el ángulo theta en radianes según las condiciones del profe
if x > 0 and y >= 0:
    theta = math.atan(y/x)
elif x == 0 and y > 0:
    theta = math.pi / 2
elif x < 0:
    theta = math.atan(y/x) + math.pi
elif x == 0 and y < 0:
    theta = 3 * math.pi / 2
elif x > 0 and y < 0:
    theta = math.atan(y/x) + 2 * math.pi
else: # Caso para (0,0)
    theta = 0

# Pasamos a grados
theta_grados = math.degrees(theta)

# Mostramos los resultados (usando los nombres de variables que pide el PDF)
print(f"r = {r:.2f}")
print(f"theta = {theta:.2f}")
print(f"theta_grados = {theta_grados:.0f}")