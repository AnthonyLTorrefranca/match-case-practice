import random

positions = [
    "Heads",
    "Tails",
]
print("Let's play a game Heads and Tails where you choose between the heads and tails👍\n")

def user_choice():
    choice = input("Input yours: ").title()
    if choice not in positions:
        print("Nah uh not in the choices\n")

    if choice in ("H", "He", "Hea", "Head", "Heads"):
        choice = "Heads"
    elif choice in ("T", "Ta", "Tai", "Tail", "Tails"):
        choice = "Tails"
    return choice

game = True
while game:
    winner_choice = random.choice(positions)
    bot_choice = random.choice(positions)
    uchoice = user_choice()
    while uchoice not in positions:
        print("Heads and Tails only!")
        uchoice = user_choice()

    match (uchoice == winner_choice, bot_choice == winner_choice,):
        case (True, True):
            print("It's a draw!\n")
        case (True, False):
            print("You win!\n")
        case (False, True):
            print("Opponent wins!\n")
        case (False, False,):
            print("No one wins!\n")

    while True:
        proceed = input("Continue? Yes or No only: ").title()
        if proceed in ("Y", "Ye", "Yes"):
            print("Let's play the heads and tails again!👍")
            break
        elif proceed in ("N", "No", "Nop", "Nope", "Not"):
            game = False
            break
        else:
            print("Nope, not in the choices!")