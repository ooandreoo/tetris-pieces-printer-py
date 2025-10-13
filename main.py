from piece.piece_one import PieceOne
from board.board import Board
import time

def main():
    print("Hello world")

    center_x = 2
    center_y = 3
    x_positions = [2,2, 1, 3]
    y_positions = [3,4, 3, 3]

    piece = PieceOne(x_positions,y_positions,center_x,center_y)

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
