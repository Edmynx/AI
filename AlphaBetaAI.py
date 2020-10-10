import chess
from math import inf
from time import sleep
import eval_function

class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth

        # parameters for each move
        # get reinitialized by each new starting move
        self.alpha = -inf
        self.beta = inf
        self.tracked_depth = 0
        self.moves_explored = {}

    def cutoff_test(self):
        return self.tracked_depth >= self.depth

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

        if self.cutoff_test():
            return eval_function.evaluation_fun(board)

        for move in board.legal_moves:
            print("1")
            board.push(move)
            self.tracked_depth += 1
            value = max(value, self.min_value(board))
            if len(board.move_stack) == 1:
                self.moves_explored[move] = value
            board.pop()
            self.tracked_depth -= 1
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

        # Base Case:
        if self.cutoff_test():
            return eval_function.evaluation_fun(board)

        for move in board.legal_moves:
            board.push(move)
            self.tracked_depth += 1
            value = min(value, self.max_value(board))
            board.pop()
            if value <= self.alpha:
                return value
            self.beta = min(self.beta, value)

        return value


    def choose_move(self, board):
        print("ggggggggggggggggggggggg")
        self.moves_explored = {}
        self.tracked_depth = 0
        self.alpha = -inf
        self.beta = inf
        value = self.max_value(board)
        print(value)

        print(self.moves_explored)
        for move, val in self.moves_explored.items():
            if val == value:
                print("this ooooooo", move)
                return move




