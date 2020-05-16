from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()

    if player == ai:
        return "Empate!"
    elif player == "piedra":
        if ai == "papel":
            return "Perdiste!"
        else:
            return "Ganaste!"
    elif player == "papel":
        if ai == "tijeras":
            return "Perdiste!"
        else:
            return "Ganaste!"
    elif player == "tijeras":
        if ai == "piedra":
            return"Perdiste!"
        else:
            return"Ganaste!"
    else:
        return"Esa no es una opcion valida. Mira bien que seleccionas"

# Entry Point
def Game():
    #
    #
    
    #
    #

    player = input("Selecciona Piedra, Papel, Tijeras -> ")

    ai = options[randint(0, 2)]
    
    winner = quienGana(player, ai)

    print(winner)
