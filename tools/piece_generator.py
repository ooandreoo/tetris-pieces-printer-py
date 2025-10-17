from piece.piece import Piece
from tools.rule_random_generator import RuleRandomGenerator

class PieceGenerator:
    def __init__(self, boardHeight, boardWidth):
        # center for start instantiating pieces, needs to be 1 row below top row because of pieces distribution of pieces
        self.center = (boardWidth//2,boardHeight-2)
        self.randomizer = RuleRandomGenerator([0,1,2,3,4,5,6],2,4)
        self.pieces_figures = [
            [(0,0),(-1,0),(1,0),(0,1)],
            [(0,0),(0,1),(1,0),(1,1)],
            [(0,0),(1,0),(0,1),(1,-1)],
            [(0,0),(0,-1),(1,0),(1,1)],
            [(0,1),(0,0),(0,-1),(0,-2)],
            [(-1,1),(0,1),(0,0),(0,-1)],
            [(0,1),(1,1),(0,0),(0,-1)]
        ]

    def get_positions(self, index):
        positions = []
        for pair in self.pieces_figures[index]:
            positions.append((pair[0]+self.center[0], pair[1]+self.center[1]))

        return positions

    def generate_piece(self):
        index = self.randomizer.generate_random_value()

        piece_positions = self.get_positions(index)

        x_coordinates, y_coordinates = zip(*piece_positions)

        piece = Piece(list(x_coordinates), list(y_coordinates), self.center[0], self.center[1])

        return piece
