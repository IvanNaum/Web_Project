class Piece:
    def __init__(self, color):
        self.color = color
        self.is_queen = False

    def __str__(self):
        return f'{self.color}p'
