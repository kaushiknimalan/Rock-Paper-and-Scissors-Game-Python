import random
import Check_Process

print("""Hi, This is Rock,Paper and scissors game.. 
You can play this game anytime and anywhere you want..
You are gonna compete with our intelligent computer which most of them has never defeated
Let's see if you can win..

""")

loops = int(input("How many rounds do you want?? "))


def time_for_player():
    players_choice = int(input("What do you wanna choose?? (1 : Rock, 2 : Paper, 3 : Scissors) "))
    return players_choice


def time_for_computer():
    computers_choice = random.randint(1, 3)
    return computers_choice


returned_points = None

i = 1
while i <= loops:
    players = time_for_player()
    computers = time_for_computer()
    if computers == players:
        print("Both values are same")
        i += 1
        continue
    elif players > 3 or computers > 3:
        print("Value must be a number or you have written the number more than 3")
        i += 1
        continue
    else:
        returned_points = Check_Process.check(computers, players)
        i += 1
        continue


if returned_points[0] > returned_points[1]:
    print(f"Player wins with the total of {returned_points[0]} beating the computer's total of {returned_points[1]}!! ")
elif returned_points[1] > returned_points[0]:
    print(f"Computer wins with the total of {returned_points[1]} beating the Player's total of {returned_points[0]}!! ")
else:
    print("It's a tie!")

print("\n Thank you for playing rock paper scissors with us..")
