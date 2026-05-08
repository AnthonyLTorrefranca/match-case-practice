import random
position = (
    "Heads",
    "Tails",
)

def game():
    winning = random.choice(position)
    bot = random.choice(position)
    print("Let's play heads and tails game!")
    while True:
        user = input("Enter your choice here: ").title()
        match user:
            case "H" | "He" | "Hea" | "Head" | "Heads":
                user = "Heads"
                break
            case "T" | "Ta" | "Tai" | "Tail" | "Tails":
                user = "Tails"
                break
            case _:
                print("Nah uh Heads or Tails only!☝️")

    match (user == winning, bot == winning):
        case (False, False):
            result = "it's a draw, none chooses the winning choice!"
        case (True, True):
            result = "it's a draw, you both won!"
        case (False, True):
            result = "you loses the bot won!"
        case (True, False):
            result = "you won the bot loses!"
    print(f"Winning choice is {winning!r}, {result}")

def proceed():
    while True:
        shall = input("Shall we continue? Yes or no only: ").title()
        match shall:
            case "Y" | "Yep" | "Yeah" | "Yes":
                flip = True
                break
            case "N" | "No" | "Nah" | "Nope":
                flip = False
                break
            case _:
                print("Nah uh Yes or No only!")
    return flip

flip = True
while flip:
    game()
    flip = proceed()