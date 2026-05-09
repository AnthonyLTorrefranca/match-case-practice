import random
position = [
    "Heads",
    "Tails",
]

scores = {
    "user": 0,
    "bot": 0,
}

def game():
    print("Welcome to the game! Where we play heads and tails")
    winning = random.choice(position)
    bot = random.choice(position)
    # user choice
    while True:
        user = input("Enter your choice: ").capitalize()
        match user:
            case "H" | "He" | "Hea" | "Head" | "Heads":
                user = "Heads"
                break
            case "T" | "Ta" | "Tai" | "Tail" | "Tails":
                user = "Tails"
                break
            case _:
                print("Nah uh☝️ Not in the choices!")
    # handles winning
    match (user == winning, bot == winning):
        case (False, False):
            result = f"it's a draw no one wins!"
        case (True, True):
            result = f"it's a draw you both won!"
            scores['user'] += 1
            scores['bot'] += 1
        case (True, False):
            result = f"You win! the bot loses!"
            scores['user'] += 1
        case (False, True):
            result = f"You lose! the bot wins!"
            scores['bot'] += 1
    print(f"Winning = {winning!r}, Bot's {bot!r}, {result}")
    scoring()

def scoring():
    user_score = scores['user']
    bot_score = scores['bot']
    while True:
        match (user_score, bot_score):
            case (0, 0):
                game()
            case (_, 5):
                print("The bot wins!")
                break
            case (5,_):
                print("You win!")
        while True:
            know = input("Want to know your scores? Yes or no only: ").capitalize()
            match know:
                case "Y" | "Ye" | "Yes" | "Yah":
                    print(f"Your score is {scores['user']}, bot's {scores['bot']}")
                    break
                case "N" | "No" | "Nope" | "Nah":
                    # print("\n")
                    game()
                case _:
                    print("Nah uh☝️ Yes or no only!")

def proceed():
    while True:
        shall = input("Shall we continue? Yes or no only: ").capitalize()
        match shall:
            case "Y" | "Ye" | "Yes" | "Yah":
                print("\t")
                game()
            case "N" | "No" | "Nope" | "Nah":
                flip = False
                break
            case _:
                print("Nah uh☝️ Yes or no only!")

    return flip

flip = True
while flip:
    game()
    flip = proceed()
