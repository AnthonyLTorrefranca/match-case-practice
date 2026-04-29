import random

positions = [
    "Heads", "Tails"
]

game = True

while game:
    print("Let's play a game called a Heads or Tails")
    winning_choice = random.choice(positions)
    bot_choice = random.choice(positions)
    user_choice = input("Enter your choice between heads and tails: ").title()
    while True:
        match (winning_choice, bot_choice, user_choice):
            case (winning_choice, bot_choice, user_choice) if winning_choice == bot_choice and winning_choice == user_choice:
                print(f"The winning is {winning_choice} your choice is {user_choice} and the opponent is {bot_choice} it's a draw")
                break
            case (winning_choice, bot_choice, user_choice) if winning_choice == bot_choice:
                print(f"The winning is {winning_choice} your choice is {user_choice} and the opponent is {bot_choice}\nThe opponent wins!")
                break
            case (winning_choice, bot_choice, user_choice) if winning_choice == user_choice:
                print(f"The winning is {winning_choice} your choice is {user_choice} and the opponent is {bot_choice}\nThe user wins")
                break
            case _:
                print("Heads or Tails only!")
                user_choice = input("Nah uh Heads or Tails only! ")
    while game:
        proceed = input("Continue playing? Yes or no only: ").title()
        match proceed:
            case "Yes":
                break
            case "No":
                game = False
            case _:
                print("Nah uh not in the choices!")