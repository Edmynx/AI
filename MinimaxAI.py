import chess
from math import inf

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth
        self.tracked_depth = 0

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
                board.pop(move)
                if self.tracked_depth >= self.depth:
                    return value

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

        return value

    def choose_move(self, board):
        self.tracked_depth = 0
        value = -inf
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            temp = value
            value = max(value, self.min_value(board))
            if value > temp:
                best_move = move
            board.pop(move)

        return best_move




