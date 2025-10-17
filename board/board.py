from piece.piece import Piece
from tools.piece_generator import PieceGenerator

import os

class Board:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.matrix = [[0 for _ in range(width)] for _ in range(height)]
        self.piece_generator = PieceGenerator(height,width)
        self.piece = None

    def add_piece(self):
        self.piece = self.piece_generator.generate_piece()

    def piece_has_room_within_matrix(self):
        piece_positions = self.piece.get_positions()

        for i in range(len(piece_positions)):
            if(self.matrix[piece_positions[0]][piece_positions[1]] == 1):
                return False
        return True

    def tick(self):
        #self.piece.rotate("right",90)
        self.piece.move()
        self.clear()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        piece_positions = self.piece.get_positions()
        piece_positions.sort()

        print("--- START OF BOARD ---")
        j = self.height-1
        for _ in range(self.height):
            line = ""
            for i in range(self.width):
                if(len(piece_positions)>0 and (i,j) in piece_positions):
                    line+=" #"
                else: # we still need to add a condition in case this position has 1 or 0
                    if self.matrix[i][j] == 0:
                        line+="  "
                    else:
                        line+=" #"
            j-=1
            print(line)
        print("--- END OF BOARD ---")

