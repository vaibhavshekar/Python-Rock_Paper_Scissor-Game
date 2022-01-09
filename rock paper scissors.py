X= input('ready to play? Y/N:  ')

from random import randint

t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]


if X=='Y':
    player = input("Rock, Paper, Scissors?:  ")
    if player == computer:
        print("Tie!", 'GAME OVER')
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player, 'GAME OVER')
        else:
            print("You win!", player, "smashes", computer, 'GAME OVER')
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player, 'GAME OVER')
        else:
            print("You win!", player, "covers", computer, 'GAME OVER')
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player, 'GAME OVER')
        else:
            print("You win!", player, "cut", computer, 'GAME OVER')
    else:
        print("That's not a valid play. Check your spelling!")


else:    
    print('Game over')
        
