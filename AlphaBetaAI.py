import chess
from math import inf


class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth
        self.alpha = -inf
        self.beta = inf
        self.tracked_depth = 0
        self.moves_explored = []

    def max_value(self, board):
        # Base Cases:
        if board.is_game_over():
            result = board.result
            if result == "1-0":
                return 1
            elif result == "0-1":
                return -1
            return 0
        value = -inf

        for move in board.legal_moves:
            board.push(move)
            self.tracked_depth += 1
            value = max(value, min_value(board))
            self.moves_explored[move] = value
            board.pop(move)
            if self.tracked_depth >= self.depth:
                return value
            if value >= self.beta:
                return value
            self.alpha = max(self.alpha, value)

        return value

    def min_value(self, board):
        # Base Case:
        if board.is_game_over():
            result = board.result
            if result == "1-0":
                return 1
            elif result == "0-1":
                return -1
            return 0
        value = inf

        for move in board.legal_moves:
            board.push(move)
            self.tracked_depth += 1
            value = min(value, max_value(board))
            board.pop(move)
            if self.tracked_depth >= self.depth:
                return value
            if value <= self.alpha:
                return value
            self.beta = min(self.beta, value)

        return value


    def choose_move(self, board):
        self.moves_explored = []
        self.tracked_depth = 0
        self.alpha = -inf
        self.beta = inf
        value = self.max_value(board)

        for move, val in self.moves_explored.items():
            if val == value:
                return move
