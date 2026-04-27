# Pedimos los datos por teclado y los convertimos a float (decimales)
omega = float(input("Introduce la velocidad angular (rad/sg): "))
radio = float(input("Introduce el radio de la trayectoria (m): "))

# Calculamos la aceleración usando la fórmula: omega al cuadrado por radio
aceleracion = (omega ** 2) * radio

# Mostramos el resultado
print(aceleracion)