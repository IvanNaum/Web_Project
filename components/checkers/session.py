import constants
from components.checkers.board import Board


class Session:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

        self.is_close = False

        self.board = Board()

    def get_data_by_user(self, user):
        if user == self.user1:
            return self.board.get_board()[::-1], constants.WHITE
        elif user == self.user2:
            return list(map(lambda x: x[::-1], self.board.get_board())), constants.BLACK

    def get_users(self):
        return self.user1, self.user2
