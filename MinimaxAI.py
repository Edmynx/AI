import chess
from math import inf
from time import sleep
import eval_function

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
            value = max(value, self.min_value(board))
            board.pop()
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
            print("1")
            board.push(move)
            self.tracked_depth += 1
            value = min(value, self.max_value(board))
            board.pop()
            if self.tracked_depth >= self.depth:
                return value

        return value

    def choose_move(self, board):
        sleep(1)
        self.tracked_depth = 0
        value = -inf
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            temp = value
            value = max(value, self.min_value(board))
            if value > temp:
                best_move = move
            board.pop()

        return best_move








