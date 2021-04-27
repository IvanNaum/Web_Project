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
        fmt_board = []
        for row in self.board:
            fmt_row = '| ' + ' | '.join(str(el or ' ') for el in row) + ' |'
            fmt_board.append('-' * len(fmt_row))
            fmt_board.append(fmt_row)
        return '\n'.join(fmt_board)

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
            if (
                self.check_piece(to_y, to_x) 
                or not self.check_same_diagonal(from_y, from_x, to_y, to_x)
                or (from_y, from_x) == (to_y, to_x)
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

    def get_eaten_pieces(self, from_y, from_x, to_y, to_x):
        eaten_pieces = []
        if abs(to_y - from_y) == 2:
            mid_y = (to_y + from_y) // 2
            mid_x = (to_x + from_x) // 2
            if self.check_piece(mid_y, mid_x) and not self.check_color(mid_y, mid_x):
                eaten_pieces.append((mid_y, mid_x))
        return eaten_pieces

    def can_move(self, from_y, from_x, to_y, to_x):
        return (to_y, to_x) in self.get_possible_moves(from_y, from_x)

    def move(self, from_y, from_x, to_y, to_x):
        if self.can_move(from_y, from_x, to_y, to_x):
            piece: Piece = self.board[from_y][from_x]

            self.board[from_y][from_x] = None

            for y, x in self.get_eaten_pieces(from_y, from_x, to_y, to_x):
                self.board[y][x] = None

            self.board[to_y][to_x] = piece

            self.change_color()

            winner = self.check_win()
            return winner

    def check_win(self):
        for from_y, from_x in product(range(constants.SIZE), repeat=2):
            if self.check_color(from_y, from_x):
                for to_y, to_x in product(range(constants.SIZE), repeat=2):
                    if self.can_move(from_y, from_x, to_y, to_x):
                        return

        return self.dif_color()

    def dif_color(self):
        return constants.WHITE if self.color == constants.BLACK else constants.BLACK

    def change_color(self):
        self.color = self.dif_color()
