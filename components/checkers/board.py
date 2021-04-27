from components.checkers.piece import Piece
import constants
from itertools import product
from math import copysign


class Board:
    def __init__(self):
        self.board = [[None] * constants.SIZE for _ in range(constants.SIZE)]
        self.color = constants.WHITE

        # заполнение поля
        for y in range(constants.SIZE):
            if y in range(3):
                color = constants.WHITE
            elif y in range(5, constants.SIZE):
                color = constants.BLACK
            else:
                continue

            for x in range(y % 2, constants.SIZE, 2):
                self.board[y][x] = Piece(color)

    def __str__(self):
        return '\n'.join([' | '.join(str(el).center(6, ' ') for el in row) for row in self.board])

    def check_piece(self, y, x):
        return type(self.board[y][x]) == Piece

    def check_empty(self, y, x):
        return self.board[y][x] is None

    @staticmethod
    def check_same_diagonal(from_y, from_x, to_y, to_x):
        return from_y + from_x == to_y + to_x or from_y - from_x == to_y - to_x

    def check_color(self, y, x):
        if not self.check_piece(y, x):
            return False

        piece: Piece = self.board[y][x]
        return self.color == piece.color

    @staticmethod
    def get_dir_y(from_y, to_y):
        return int(copysign(1, to_y - from_y))

    def get_possible_moves(self, from_y, from_x):
        possible_moves = []

        if not self.check_color(from_y, from_x):
            return possible_moves

        piece: Piece = self.board[from_y][from_x]

        for to_y, to_x in product(range(constants.SIZE), repeat=2):
            if not (
                self.check_empty(to_y, to_x)
                and self.check_same_diagonal(from_y, from_x, to_y, to_x)
            ):
                continue

            if not piece.is_queen:
                if abs(to_y - from_y) == 1:
                    dir_y = self.get_dir_y(from_y, to_y)
                    if dir_y == piece.dir_y:
                        possible_moves.append((to_y, to_x))

                elif abs(to_y - from_y) == 2:
                    mid_y = (to_y + from_y) // 2
                    mid_x = (to_x + from_x) // 2 
                    if self.check_piece(mid_y, mid_x) and not self.check_color(mid_y, mid_x):
                        possible_moves.append((to_y, to_x))

            else:
                pass
                # TODO

        return possible_moves

    def can_move(self, from_y, from_x, to_y, to_x):
        return (to_y, to_x) in self.get_possible_moves(from_y, from_x)

    def move(self, from_y, from_x, to_y, to_x):
        if self.can_move(from_y, from_x, to_y, to_x):
            piece: Piece = self.board[from_y][from_x]

            self.board[from_y][from_x] = None
            self.board[to_y][to_x] = piece

            self.change_color()

    def change_color(self):
        self.color = constants.WHITE if self.color == constants.BLACK else constants.BLACK
