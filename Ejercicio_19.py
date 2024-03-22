def resultado_set(juegos_A, juegos_B):
    # Verificar si el resultado es válido
    if abs(juegos_A - juegos_B) > 2 or (juegos_A > 7 or juegos_B > 7):
        return "Resultado inválido"
    
    # Verificar si el set todavía no termina
    if juegos_A < 6 and juegos_B < 6:
        return "El set todavía no ha terminado"
    
    # Verificar si uno de los jugadores ganó por llegar a 6 juegos
    if juegos_A >= 6 or juegos_B >= 6:
        # Verificar si se cumplen las condiciones para declarar un ganador
        if abs(juegos_A - juegos_B) >= 2:
            if juegos_A > juegos_B:
                return "El jugador A ganó el set"
            else:
                return "El jugador B ganó el set"
        # Verificar si el set se define en un último juego (empate a 6 juegos)
        elif juegos_A == juegos_B == 6:
            return "El set se define en un último juego: 7-6"
        else:
            return "El set todavía no ha terminado"

# Solicitar al usuario la cantidad de juegos ganados por cada jugador
juegos_A = int(input("Ingrese la cantidad de juegos ganados por el jugador A: "))
juegos_B = int(input("Ingrese la cantidad de juegos ganados por el jugador B: "))

# Obtener el resultado del set
resultado = resultado_set(juegos_A, juegos_B)

# Mostrar el resultado
print(resultado)
