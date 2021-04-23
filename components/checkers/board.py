import constants
from components.checkers.piece import Piece


class Board:
    def __init__(self):

        self.board = [[None] * constants.SIZE for _ in range(constants.SIZE)]
        self.cur_color = constants.WHITE

        # Заполнение поля
        for item, color in enumerate([constants.WHITE, constants.BLACK]):
            for i in range(3):
                for j in range((i + item) % 2, constants.SIZE, 2):
                    self.board[i][j] = Piece(color)
            self.board = self.board[::-1]

    def __str__(self):
        return '\n'.join([' | '.join(str(j).center(6, ' ') for j in i) for i in self.board])

    @staticmethod
    def check_pos(y, x):
        return x < constants.SIZE and y < constants.SIZE

    def check_color(self, y, x):
        element = self.board[y][x]
        return self.cur_color == element.color

    @staticmethod
    def check_same_diagonal(from_y, from_x, to_y, to_x):
        return from_x + from_y == to_y + to_x

    def check_piece(self, y, x):
        return type(self.board[y][x]) == Piece

    def check_empty(self, y, x):
        return self.board[y][x] is None

    def check_move(self, from_y, from_x, to_y, to_x):
        if all([
            self.check_pos(from_y, from_x),
            self.check_pos(to_y, to_x),

            self.check_piece(from_y, from_x),
            self.check_empty(to_y, to_x),

            self.check_color(from_y, from_x),
            self.check_same_diagonal(from_y, from_x, to_y, to_x)
        ]):
            piece: Piece = self.board[from_y][from_x]
            if piece.is_queen:
                return True
            else:
                pass

    def move(self, old_pos, new_pos):
        pass

    def get_board(self):
        return self.board.copy()
