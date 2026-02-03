import random

#hola

# Colores disponibles
colores = ['R', 'G', 'B', 'Y', 'O', 'P']  # Rojo, Verde, Azul, Amarillo, Naranja, Púrpura

# Generar código secreto
codigo = random.choices(colores, k=4)

print("¡Bienvenido a Mastermind!")
print("Colores disponibles: R, G, B, Y, O, P")
print("Adivina el código de 4 colores. Ejemplo: RGBY")

intentos = 0
while True:
    intento = input("Introduce tu intento: ").upper()
    intentos += 1

    if len(intento) != 4 or any(c not in colores for c in intento):
        print("Entrada inválida. Debe ser 4 letras de los colores disponibles.")
        continue

    # Contar aciertos en posición
    aciertos_pos = sum(c1 == c2 for c1, c2 in zip(codigo, intento))

    # Contar aciertos de color (sin contar los ya acertados)
    aciertos_color = 0
    for c in set(intento):
        aciertos_color += min(intento.count(c), codigo.count(c))
    aciertos_color -= aciertos_pos  # quitar los ya contados como posición

    print(f"Aciertos en posición: {aciertos_pos}, Aciertos de color: {aciertos_color}")

    if aciertos_pos == 4:
        print(f"¡Felicidades! Has adivinado el código en {intentos} intentos.")
        break
