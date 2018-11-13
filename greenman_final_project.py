# Trent Greenman
#CS 21, Fall 2018
#Program: Tennis

from random import random
def play_game(probA, verbose):
    A = 0
    B = 0
    points = ["0","15","30","40"]
    while A <= 3 and B <= 3 and (A != 3 or B != 3) and verbose:
        print("Current Score:", points[A], "-", points[B])
        if random() < probA:
            A += 1
        else:
            B += 1
    while (A > 3 or B > 3 or (A == 3 and B == 3)) and verbose:
        if A == B:
            print("Current Score: deuce")
        elif A - B == 1:
            print("Current Score: advantage Player A")
        elif B - A == 1:
            print("Current Score: advantagr Player B")
        elif B - A >= 2:
            print("Winner: Player B")
            print("")
            return "B"
        elif A - B >= 2:
            print("Winner: Player A")
            print("")
            return "A"
        if random() < probA:
            A += 1
        else:
            B += 1
    # Play game that does not display scores
    while A <= 3 and B <= 3 and (A != 3 or B != 3) and not(verbose):
        if random() < probA:
            A += 1
        else:
            B += 1
    while (A > 3 or B > 3 or (A == 3 and B == 3)) and not(verbose):
        if A - B >= 2:
            return "A"
        elif B - A >= 2:
            return "B"
        if random() < probA:
            A += 1
        else:
            B += 1

def play_tiebreak(probA, verbose):
    A = 0
    B = 0
    if verbose == True:
        print("TIEBREAK GAME")
    while not(verbose):
        if A - B >= 2 and A >= 7:
            return 7, 6
        elif B - A >= 2 and B >= 7:
            return 6, 7
        if random() < probA:
            A += 1
        else:
            B += 1
    while verbose:
        print("Current Score:", A, "-", B)
        if A - B >= 2 and A >= 7:
            return 7, 6
        elif B - A >= 2 and B >= 7:
            return 6, 7
        if random() < probA:
            A += 1
        else:
            B += 1
        
# tiebreak default is true and verbose default is false
def play_set(probA, tiebreak, verbose):
    Awins = 0
    Bwins = 0
    winner = ""
    while not(verbose):
        winner = play_game(probA, verbose)
        if winner == "A":
            Awins += 1
        elif winner == "B":
            Bwins += 1
        if Awins >= 6 and Awins - Bwins >= 2:
            return Awins, Bwins
        elif Bwins >= 6 and Bwins - Awins >= 2:
            return Awins, Bwins
        if Awins == 6 and Bwins == 6 and tiebreak:
            return play_tiebreak(probA, verbose)
    while verbose:
        print("Set Score:", Awins, "-", Bwins)
        winner = play_game(probA, verbose)
        if winner == "A":
            Awins += 1
        elif winner == "B":
            Bwins += 1
        if Awins >= 6 and Awins - Bwins >= 2:
            return Awins, Bwins
        elif Bwins >= 6 and Bwins - Awins >= 2:
            return Awins, Bwins
        if Awins == 6 and Bwins == 6 and tiebreak:
            return play_tiebreak(probA, verbose)
        
def play_match(probA):
    set_num = 1
    Asets = 0
    Bsets = 0
    Awins = 0
    Bwins = 0
    # change verbose and tiebreak here
    tiebreak = True
    verbose = False
    while set_num <= 2:
        print("Set Num:", set_num)
        print("A wins:", Awins)
        print("B wins:", Bwins) 
        Asets, Bsets = play_set(probA, tiebreak, verbose)
        if Asets > Bsets:
            Awins += 1
        else:
            Bwins += 1
        set_num += 1
        print("After A wins:", Awins)
        print("After B wins:", Bwins)
        if Awins == 2:
            return "A"
        elif Bwins == 2:
            return "B"
    while set_num == 3 and Awins == Bwins:
        print("Set Num:", set_num)
        print("A wins:", Awins)
        print("B wins:", Bwins)
        tiebreak == False
        Asets, Bsets = play_set(probA, tiebreak, verbose)
        if Asets > Bsets:
            return "A"
        else:
            return "B"

def print_intro():
    print("This program simulates a tennis game between two players,")
    print("Player A and Player B. It will tell you the scores and how")
    print("many games each player wins. Have fun!")
    print("")
    
def get_inputs():
    probA = 2
    while type(probA) != float or probA < 0 or probA > 1:
        try:
            probA = float(input("Enter the probability that A will"
                                " win each point: "))
            if probA > 1:
                print("The probability must be between 0 and 1.")
            if probA < 0:
                print("The probability must be between 0 and 1.")
        except ValueError:
            print("The number of games must be a real number.")
    return probA

def print_summary(winner):
    if winner == "A":
        print("Congrats Player A! You Won!")
    elif winner == "B":
        print("Congrats Player B! You Won!")

def main():
    print_intro()
    probA = get_inputs()
    winner = play_match(probA)
    print_summary(winner)
main()

    

