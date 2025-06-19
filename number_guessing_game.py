logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

import random
print(logo)

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1,100)


def game_function ():
    print(f"Psst: the number is {number}")
    is_game_over = False
    difficulty = input("Choose the level of difficulty: Easy or Hard ?").lower()
    if difficulty == "hard":
        life = 5
    if difficulty == "easy":
        life = 10
    answer = int(input(f"You have {life} attempts to guess the number"))

    while not is_game_over:
        if life == 0:
            is_game_over = True

        elif life > 0:
            if answer > number:
                life -= 1
                print("Too High")
                if life > 1:
                    answer = int(input(f"You have {life} attempts to guess the number"))
                if life == 1:
                    answer = int(input(f"You have {life} attempt to guess the number"))
            elif answer < number:
                life -= 1
                print("Too Low")
                if life > 1:
                    answer = int(input(f"You have {life} attempts to guess the number"))
                if life == 1:
                    answer = int(input(f"You have {life} attempt to guess the number"))
            else:
                print("You guess correctly")
                is_game_over = True


game_function()
restart = input("Do you want to restart the game? Y or N").lower()
if restart == "y":
    game_function()
else:
    print("Bye")








