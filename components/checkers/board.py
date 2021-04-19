from components.checkers.piece import Piece


class Board:
    SIZE = 8
    WHITE = 'W'
    BLACK = 'B'

    def __init__(self):
        self.border = [[None for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        # Заполнение поля
        for item, color in enumerate([self.WHITE, self.BLACK]):
            for i in range(3):
                for j in range((i + item) % 2, self.SIZE, 2):
                    self.border[i][j] = Piece(color)
            self.border = self.border[::-1]

    def __str__(self):
        return '\n'.join([' | '.join(str(j).center(6, ' ') for j in i) for i in self.border])


if __name__ == '__main__':
    board = Board()
    print(board)
