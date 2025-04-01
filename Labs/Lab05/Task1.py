import random

# Define piece values
piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 1000,
                'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -1000, '.': 0}

# 8x8 chess board (Initial position)
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def evaluate_board(board):
    # Returns a score based on material balance (simplistic evaluation).
    return sum(piece_values[board[row][col]] for row in range(8) for col in range(8))

def get_legal_moves(board, color):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if (color == 'white' and piece.isupper()) or (color == 'black' and piece.islower()):
                moves.extend(generate_piece_moves(board, row, col, piece))
    return moves

# Returns a list of possible moves for a given piece.
def generate_piece_moves(board, row, col, piece):
    moves = []
    directions = {
        'P': [(1, 0)], 'p': [(-1, 0)],  # Pawns (simplified, no captures)
        'N': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)],  # Knights
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishops
        'R': [(1, 0), (-1, 0), (0, 1), (0, -1)],  # Rooks
        'Q': [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)],  # Queen
        'K': [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]  # King
    }
    
    if piece.upper() in directions:
        for dr, dc in directions[piece.upper()]:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < 8 and 0 <= new_c < 8:  # Stay in bounds
                if board[new_r][new_c] == '.' or board[new_r][new_c].islower() if piece.isupper() else board[new_r][new_c].isupper():
                    moves.append(((row, col), (new_r, new_c)))
    
    return moves

def apply_move(board, move):
    new_board = [row[:] for row in board]
    (r1, c1), (r2, c2) = move
    new_board[r2][c2] = new_board[r1][c1]
    new_board[r1][c1] = '.'
    return new_board

def beam_search(board, color='white', beam_width=3, depth=3):
    beams = [(board, [])]

    for _ in range(depth):
        new_beams = []
        for current_board, move_seq in beams:
            legal_moves = get_legal_moves(current_board, color)
            
            # Evaluate and select top beam_width moves
            scored_moves = []
            for move in legal_moves:
                new_board = apply_move(current_board, move)
                score = evaluate_board(new_board)
                scored_moves.append((score, move, new_board))
            
            # Keep top beam_width moves
            scored_moves.sort(reverse=True, key=lambda x: x[0])
            top_moves = scored_moves[:beam_width]
            
            for score, move, new_board in top_moves:
                new_beams.append((new_board, move_seq + [move]))

        beams = new_beams  # Keep best candidates

    # Return best move sequence
    best_board, best_moves = max(beams, key=lambda x: evaluate_board(x[0]))
    best_score = evaluate_board(best_board)
    return best_moves, best_score

best_moves, best_score = beam_search(board, color='white', beam_width=3, depth=3)
print("Best Move Sequence:", best_moves)
print("Evaluation Score:", best_score)
