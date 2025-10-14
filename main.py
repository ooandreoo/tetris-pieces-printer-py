from piece.piece import Piece
from board.board import Board
import time

def main():
    print("Hello world")

    center_x = 2
    center_y = 2
    x_positions = [1,2, 2, 3, 0]
    y_positions = [2,2, 3, 2, 2]

    piece = Piece(x_positions,y_positions,center_x,center_y)

    board = Board(5,5)

    board.add_piece(piece)

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
