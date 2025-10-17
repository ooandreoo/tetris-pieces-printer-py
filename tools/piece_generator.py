class PieceGenerator:
    def __init__(boardHeight, boardWidth):
        # center for start instantiating pieces, needs to be 1 row below top row because of pieces distribution of pieces
        self.center = (boardWidth//2,boardHeight-2)
        self.pieces_figures = [
            [(0,0),(-1,0),(1,0),(0,1)],
            [(0,0),(0,1),(1,0),(1,1)],
            [(0,0),(1,0),(0,1),(1,-1)],
            [(0,0),(0,-1),(1,0),(1,1)],
            [(0,1),(0,0),(0,-1),(0,-2)],
            [(-1,1),(0,1),(0,0),(0,-1)],
            [(0,1),(1,1),(0,0),(0,-1)]
        ]
