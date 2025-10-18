from piece.piece import Piece
from tools.piece_generator import PieceGenerator

import os
import time

class Board:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.matrix = [[0 for _ in range(height)] for _ in range(width)]
        self.piece_generator = PieceGenerator(height,width)
        self.piece = None

    def add_piece(self):
        self.piece = self.piece_generator.generate_piece()

    def piece_reached_bottom(self):
        for point in self.piece.get_positions():
            if(point[1] == 0):
                return True
        return False

    def piece_has_room_within_matrix(self):
        # not used yet
        piece_positions = self.piece.get_positions()

        for i in range(len(piece_positions)):
            if(self.matrix[piece_positions[0]][piece_positions[1]] == 1):
                return False
        return True

    def start_loop(self):
        while True:
            self.tick()
            self.clear()
            self.draw()
            time.sleep(0.5)


    def tick(self):
        #self.piece.rotate("right",90)
        if(self.piece == None or self.piece_reached_bottom()):
            self.add_piece()
        else:
            self.piece.move()
            self.piece.rotate("right",90)
            #self.piece.move()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        piece_positions = self.piece.get_positions()
        piece_positions.sort()

        print("--- START OF BOARD ---")
        j = self.height-1
        for _ in range(self.height):
            line = ""
            #print(len(self.matrix))
            for i in range(self.width):
                #print(i,j)
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

