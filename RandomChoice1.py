import random

position = [
    "Heads",
    "Tails",
]

def game():
    winning = random.choice(position)
    user = input("Enter your choice between heads and tails: ").title()
    bot = random.choice(position)
    while True:
        match user:
            case "H" | "He" | "Hea" | "Head" | "Heads":
                user = "Heads"
                break
            case "T" | "Ta" | "Tai" | "Tail" | "Tails":
                user = "Tails"
                break
            case _:
                print("Not in the choices☝️")
                user = input("Enter your choice between heads and tails: ").title()

    while True:
        match (user == winning, bot == winning):
            case (False, False):
                result = "is a draw, None won!"
            case (True, True):
                result = "is a draw!"
            case (True, False):
                result = "is you won! The bot loses"
            case (False, True):
                result = "bot won! You loses"
        print(f"Winning is {winning!r}, Bot's choice {bot!r}. The result {result}\n")
        break

def proceed():
    while True:
        shall = input("Shall we proceed? Yes or no only: ").title()
        match shall:
            case "Y" | "Ye" | "Yes" | "Yep":
                print("Here we go!\n")
                return True
            case "N" |"No" |"Nope" |"Nah" :
                return False
                break
            case _:
                print("Nope Yes or No only!")
trulse = True
while trulse:
    print("Welcome to the game! Where we play head and tails, the winning choice is random. Choose between both.")
    game()
    trulse = proceed()
