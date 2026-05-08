import random
position = [
    "Heads",
    "Tails",
]

def game():
    winning = random.choice(position)
    bot = random.choice(position)
    print("\nWelcome to the game! Let's play a heads and tail.")
    while True:
        result = "test"
        user = input("Enter your choice: ").title()
        match user:
            case "H" | "He" | "Hea" | "Head" | "Heads":
                user = "Heads"
                break
            case "T" | "Ta" | "Tai" | "Tail" | "Tails":
                user = "Tails"
                break
            case _:
                print("Nah uh👆 not in the choices")
    match (user == winning, bot == winning):
        case (False, False):
            result = "It's a draw no one wins!"
        case (True, True):
            result = "It's a draw you both won!"
        case (False, True):
            result = "You lose! Bot wins!"
        case (True, False):
            result = "You win! Bot loses!"
    return print(f"{winning!r} is the winning choice!\nBot's choice = {bot!r}, Yours is {user!r}\n{result}")

def shall():
    while True:
        flip = input("Shall we continue the game? ").title()
        match flip:
            case "Y" | "Ye" | "Yes" | "Yesh" | "Yah":
                game()
            case "N" | "No" | "No" | "Nah" | "Nope":
                flip = False
                break
            case _:
                print("Yes or no only!")


flip = True
while flip:
    game()
    flip = shall()
    break