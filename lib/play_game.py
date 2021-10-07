from .board import *


class PlayGame:

    dicton = {"apple": "red", "grape": "purple", "orange": "orange"}

    def start():
        print("Welcome to TIC TAC TOE!")
        Board.display_board()
