from components.checkers.piece import Piece
import constants


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
        return abs(from_x - from_y) == abs(to_x - to_y)

    def check_color(self, y, x):
        if not self.check_piece(y, x):
            return False

        piece: Piece = self.board[y][x]
        return self.color == piece.color

    def check_dir_y(self, from_y, from_x, to_y, to_x):
        if not self.check_color(from_y, from_x):
            return False

        piece: Piece = self.board[from_y][from_x]
        if piece.is_queen:
            return True

        dir_y = self.get_dir_y(from_y, to_y)
        return dir_y == piece.dir_y

    def check_move(self, from_y, from_x, to_y, to_x):
        if (
            self.check_piece(from_y, from_x)
            and self.check_empty(to_y, to_x)
            and self.check_color(from_y, from_x)
            and self.check_same_diagonal(from_y, from_x, to_y, to_x)
        ):
            piece: Piece = self.board[from_y][from_x]
            if piece.is_queen:
                return True

            if not self.check_dir_y(from_y, from_x, to_y, to_x):
                return False

            eaten_pieces_count = len(
                self.get_eaten_pieces_positions(from_y, from_x, to_y, to_x))
            return eaten_pieces_count + 1 == abs(from_x - to_x) == abs(from_y - from_y)

    @staticmethod
    def get_dir_y(from_y, to_y):
        return (to_y - from_y) // abs(to_y - from_y)

    @staticmethod
    def get_dir_x(from_x, to_x):
        return (to_x - from_x) // abs(to_x - from_x)

    def get_eaten_pieces_positions(self, from_y, from_x, to_y, to_x):
        eaten_pieces_positions = []

        dir_y = self.get_dir_y(from_y, to_y)
        dir_x = self.get_dir_x(from_x, to_x)

        for n in range(1, abs(to_x - from_x)):
            # смещение по осям пропорционально (1:1),
            # поэтому достаточно одной переменной
            y = to_y + dir_y * n
            x = to_x + dir_x * n
            if self.check_piece(y, x):
                eaten_pieces_positions.append((y, x))

        return eaten_pieces_positions

    def move(self, from_y, from_x, to_y, to_x):
        if self.check_move(from_y, from_x, to_y, to_x):
            piece: Piece = self.board[from_y][from_x]

            for y, x in [(from_y, from_x), *self.get_eaten_pieces_positions(from_y, from_x, to_y, to_x)]:
                self.board[y][x] = None

            self.board[to_y][to_x] = piece

            self.change_color()

    def get_board(self):
        return self.board.copy()

    def change_color(self):
        if self.color == constants.WHITE:
            self.color = constants.BLACK
        else:
            self.color = constants.WHITE
