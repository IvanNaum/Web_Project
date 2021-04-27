import constants


class Piece:
    def __init__(self, color):
        self.color = color
        self.dir_y = 1 if self.color == constants.WHITE else -1
        self.is_queen = False

    def __str__(self):
        return f'{self.color}p'
