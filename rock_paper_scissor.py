print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

import random

def play():
    user = input("What do you want to choose between 'r' for rock, 'p' for paper, and 's' for scissors?: ")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You and the computer have both chosen {}. It's a TIE!!!.".format(computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You WON!!!.".format(user, computer)

    return "You have chosen {} and the computer has chosen {}. You LOST :{ !!!.".format(user, computer)

def is_win(player, opponent):
    # if the player beats the opponent, return true.
    # the winning conditions are: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

if __name__ == '__main__':
    print(play())