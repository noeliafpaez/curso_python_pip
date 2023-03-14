import random

#Defino primero para el juego una función responsable de obtener la opción que escoja el usuario y la computadora, como para encerrar el primer bloque de código.
def choose_options():
    options = ("piedra", "papel", "tijeras")
    user_option = input("piedra, papel o tijeras => ")
    user_option = user_option.lower()
   
    if not user_option in options:
        print("Esa opción no es válida")
        return None, None
   
    computer_option = random.choice(options)
   
    print("Opción usuario =>", user_option)
    print("Opción computadora =>", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option,user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    if user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra => Ganaste!")
            user_wins += 1
        else:
            print("tijeras gana a papel => Ganó la computadora!")
            computer_wins += 1
    elif user_option == "piedra":
        if computer_option == "tijeras":
            print("piedra gana a tijeras => Ganaste!")
            user_wins += 1
        else:
            print("papel gana a piedra => Gana la computadora!")
            computer_wins += 1
    elif user_option == "tijeras":
        if computer_option == "papel":
            print("tijeras gana a papel => Ganaste!")
            user_wins += 1
        else:
            print("piedra gana a tijeras => Gana la computadora!")
            computer_wins += 1
    return user_wins, computer_wins

#Ahora debo crear una función principal que ejecute todo nuestro juego, esto me hace más fácil de leer y mantener.
def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1
    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)
        print("user_wins =", user_wins)
        print("computer_wins =", computer_wins)

        rounds += 1
    
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        if user_wins == 2:
            print("El ganador es el usuario")
            break
        if computer_wins == 2:
            print("El ganador es la computadora")
            break
    
run_game()

#Las funciones nos permiten mantenibilidad en el código, ademñas nos ayudan a separar responsabilidades, lo cual es una buena práctica.
#"""
#RETO:
#def choose_winner(user_wins, computer_wins):
#  if user_wins == 2:
#    print("El ganador es el usuario")
#    exit()
#  if computer_wins == 2:
#    print("El ganador es la computadora")
#    exit()
#"""