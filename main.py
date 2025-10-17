from piece.piece import Piece
from board.board import Board
import time

def main():
    print("Hello world")



    board = Board(5,5)
    board.add_piece()

    board.clear()
    board.draw()
    time.sleep(1)
    board.tick()
    board.draw()
    time.sleep(1)
    board.tick()
    board.draw()
    time.sleep(1)
    board.tick()
    board.draw()

if __name__ == "__main__":
    main()
