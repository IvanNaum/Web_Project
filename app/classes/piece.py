from app.constants import *


class Piece:
    def __init__(self, color):
        self.color = color
        self.dir_y = 1 if self.color == WHITE else -1
        self.is_queen = False

    def __str__(self):
        return self.color
