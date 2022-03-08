import random
print("Play Rock,Paper,Scissor")
print("Enter your choice:")
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
comp_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?")
 
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            comp_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            comp_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            comp_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"Comp:{comp_score}")
        print(f"Plaer:{player_score}")
        break