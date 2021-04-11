

game_values = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

points = [0, 0]


def check(computers, players):
    if computers == 1 and players == 2 or computers == 2 and players == 1:

        print(" ")
        print(f"Player's choice : {game_values[players]}")
        print(f"Computer's choice : {game_values[computers]}")
        print(" ")

        if computers == 2:
            print("Computer gets a point")
            print(" ")
            points[1] += 1
        else:
            print("Player gets a point")
            print(" ")
            points[0] += 1

    elif computers == 2 and players == 3 or computers == 3 and players == 2:

        print(" ")
        print(f"Player's choice : {game_values[players]}")
        print(f"Computer's choice : {game_values[computers]}")
        print(" ")

        if computers == 3:
            print("Computer gets a point")
            print(" ")
            points[1] += 1
        else:
            print("Player gets a point")
            print(" ")
            points[0] += 1

    elif computers == 1 and players == 3 or computers == 3 and players == 1:

        print(" ")
        print(f"Player's choice : {game_values[players]}")
        print(f"Computer's choice : {game_values[computers]}")
        print(" ")

        if computers == 1:
            print("Computer gets a point")
            print(" ")
            points[1] += 1
        else:
            print("Player gets a point")
            print(" ")
            points[0] += 1
    return points
