"""Entry point
"""
from board import Board
from backtrack import Backtrack
from time import time


def main():
    print("+------------------------------------------+\n")

    GAME = Board()
    print(GAME)

    print("+------------------------------------------+\n")
    GAME.fill()

    print("+------------------------------------------+\n")
    print(GAME)

    print("+------------------------------------------+\n")
    SOLVER = Backtrack(GAME._board, GAME._length)
    SOLVER.run()
    print(GAME)

    print("+------------------------------------------+\n")


if __name__ == '__main__':
    main()
