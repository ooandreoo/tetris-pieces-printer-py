class PieceOne:
    def __init__(self, x_positions, y_positions, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.x_positions = x_positions
        self.y_positions = y_positions

    def get_positions(self):
        return list(zip(self.x_positions,self.y_positions))

    def move(self):
        self.y_positions = [x-1 for x in self.y_positions]
