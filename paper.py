from random import randint

objs = ["Rock", "Paper", "Scissor"]

computer = objs[randint(0, 2)]

playing = True

while playing:
    player = input("Rock, Paper or Scissor ?    ")
    if player == "Rock":
        if computer == "Scissor":
            print("You Won", player, "Beats", computer)
        elif computer == "Paper":
            print("You Lose", computer, "Beats", player)
        else:
            print("DRAW")
    elif player == "Paper":
        if computer == "Rock":
            print("You Won", player, "Beats", computer)
        elif computer == "Scissor":
            print("You Lose", computer, "Beats", player)
        else:
            print("DRAW")
    elif player == "Scissor":
        if computer == "Paper":
            print("You Won", player, "Beats", computer)
        elif computer == "Rock":
            print("You Lose", computer, "Beats", player)
        else:
            print("DRAW")
    else:
        print("Check your spelling", end="\n")

    computer = objs[randint(0, 2)]
    key = input(
        """
    1. To keep Playing Press Enter
    2. To Quit Press input Q
    """
    )
    if key == "q":
        playing = False

print("Thank You For Playing!")

