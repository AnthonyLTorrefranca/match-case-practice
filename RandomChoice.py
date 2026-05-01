import random

positions = [
    "Heads", "Tails"
]

game = True

while game:
    print("\nLet's play a game called a Heads or Tails")
    winning_choice = random.choice(positions)
    bot_choice = random.choice(positions)
    user_choice = input("Enter your choice between heads and tails: ").title()
    while user_choice not in positions:
        print("Nah uh Heads or Tails only!!")
        user_choice = input("Enter your choice between heads and tails:  ").title()
    match (user_choice == winning_choice, bot_choice == winning_choice):
        case (True, True):
            print(f"\nThe selected winning choice is {winning_choice!r}\nUser's choice {user_choice!r} and bot's choice {bot_choice!r} It's a draw!")
        case (True, False):
            print(f"\nThe selected winning choice is {winning_choice!r}\nBot's choice is {bot_choice!r} and user's choice is {user_choice!r} the user wins!")
        case (False, True):
            print(f"\nThe selected winning choice is {winning_choice!r}\nBot's choice is {bot_choice!r} and user's choice is {user_choice!r} the opponent wins!")
        case (False, False):
            print("None chose the winning choice it's a draw!")
    while True:
        proceed = input("\nContinue playing? Yes or no only: ").title()
        match proceed:
            case "Yes":
                break
            case "No":
                game = False
                break
            case _:
                print("\nNah uh not in the choices!")