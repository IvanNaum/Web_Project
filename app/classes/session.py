from app.constants import *
from app.classes.board import Board
from app.classes.piece import Piece


class Session:
    def __init__(self, user1):
        self.user1 = user1
        self.user2 = None

        self.is_close = False

        self.board = Board()

    def set_user2(self, user):
        self.user2 = user

    def get_data_by_user(self, user):
        if user == self.user1:
            return self.board.board[::-1], WHITE
        elif user == self.user2:
            return [row[::-1] for row in self.board.board], BLACK

    def get_users(self):
        return self.user1, self.user2

    def get_pieces(self, user):
        pieces = []

        board, color = self.get_data_by_user(user)
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if type(item) == Piece:
                    pieces.append({
                        'color': item.color,
                        'is_queen': item.is_queen,
                        'row': i,
                        'col': j
                    })
        return pieces, color, self.board.color

    def move(self, from_x, from_y, to_x, to_y, user):
        if user == self.user1:
            self.board.move(
                SIZE - from_y - 1, from_x,
                SIZE - to_y - 1, to_x
            )
        elif user == self.user2:
            self.board.move(
                from_y, SIZE - from_x - 1,
                to_y, SIZE - to_x - 1
            )
