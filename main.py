# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import functools
import sys

from gomoku import Gomoku


def main():
    print("Welcome to the Gomoku game!")
    while True:
        print("You can input your move as x, y (x, y between 0-14) to play the game")
        game = Gomoku()
        val = game.play()
        if val != 0:
            v = input("Do you want to keep playing? ")
            if v == 'q' or v == 'Q':
                print("Bye!")
                sys.exit()


if __name__ == '__main__':
    main()
