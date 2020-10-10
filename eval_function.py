import chess


def evaluation_fun(board):
    pawn_val = 1 * len(list(board.pieces(chess.PAWN, chess.WHITE)))
    knight_val = 3 * len(list(board.pieces(chess.KNIGHT, chess.WHITE)))
    bishop_val = 3 * len(list(board.pieces(chess.BISHOP, chess.WHITE)))
    rook_val = 5 * len(list(board.pieces(chess.ROOK, chess.WHITE)))
    queen_val = 9 * len(list(board.pieces(chess.QUEEN, chess.WHITE)))
    king_val = 13 * len(list(board.pieces(chess.KING, chess.WHITE)))

    return pawn_val + knight_val + bishop_val + rook_val + queen_val + king_val