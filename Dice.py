from random import *

def playOnce():
    roll = randint(1,6)
    print roll


def main():
    roll_again = True
    while roll_again:
        playOnce()
        ans = raw_input("Would you like to go again")
        if ans != 'y':
            roll_again = False

main()
