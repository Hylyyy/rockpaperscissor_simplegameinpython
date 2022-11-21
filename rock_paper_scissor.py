print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

import random
import math

def play():
    user = input("What do you want to choose between 'r' for rock, 'p' for paper, and 's' for scissors?: ")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # if the player beats the opponent, return true.
    # the winning conditions are: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # will play continuosly agasint the computer until someone wins on the best of n games
    # to win, one must win ceilin(n/2) games like 2/3, 3/5, 4/7
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # if TIE
        if result == 0:
            print('You and the computer have both chosen {}. It is a TIE!!! \n'.format(user))
        # if you WIN
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You WON!!!.\n.'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You LOST :[ !!!.\n'.format(user, computer))
        print('/n')

    if player_wins > computer_wins:
        print('===HOORAY!. YOU HAVE WON THE BEST OF {} GAMES!!!.'.format(n))
    else:
        print('AWWW :[ THE COMPUTER HAS WON THE BEST OF {} GAMES!!!. BETTER LUCK NEXT TIME!!!.'.format(n))


if __name__ == '__main__':
    print(play())
    play_best_of(3) # 2