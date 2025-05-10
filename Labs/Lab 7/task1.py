import copy
import random

EMPTY = '.'
WHITE = 'W'
BLACK = 'B'

class Checkers:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = WHITE

    def create_board(self):
        board = [[EMPTY for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = BLACK
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = WHITE
        return board

    def print_board(self):
        print("  " + " ".join(map(str, range(8))))
        for i, row in enumerate(self.board):
            print(i, " ".join(row))

    def get_valid_moves(self, player):
        moves = []
        directions = [(-1, -1), (-1, 1)] if player == WHITE else [(1, -1), (1, 1)]
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == player:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == EMPTY:
                            moves.append(((r, c), (nr, nc)))
                        # capture
                        er, ec = r + 2 * dr, c + 2 * dc
                        if (0 <= er < 8 and 0 <= ec < 8 and
                            self.board[nr][nc] in [WHITE, BLACK] and self.board[nr][nc] != player and
                            self.board[er][ec] == EMPTY):
                            moves.append(((r, c), (er, ec)))
        return moves

    def apply_move(self, move):
        (r1, c1), (r2, c2) = move
        piece = self.board[r1][c1]
        self.board[r1][c1] = EMPTY
        self.board[r2][c2] = piece
        if abs(r2 - r1) == 2:
            self.board[(r1 + r2) // 2][(c1 + c2) // 2] = EMPTY

    def is_game_over(self):
        return not self.get_valid_moves(WHITE) or not self.get_valid_moves(BLACK)

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or self.is_game_over():
            return self.evaluate_board(), None

        player = BLACK if maximizing else WHITE
        moves = self.get_valid_moves(player)
        best_move = None

        if maximizing:
            max_eval = float('-inf')
            for move in moves:
                temp = copy.deepcopy(self)
                temp.apply_move(move)
                evaluation = temp.minimax(temp.board, depth - 1, alpha, beta, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in moves:
                temp = copy.deepcopy(self)
                temp.apply_move(move)
                evaluation = temp.minimax(temp.board, depth - 1, alpha, beta, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate_board(self):
        white_count = sum(row.count(WHITE) for row in self.board)
        black_count = sum(row.count(BLACK) for row in self.board)
        return black_count - white_count

    def play(self):
        while not self.is_game_over():
            self.print_board()
            if self.current_player == WHITE:
                print("Your move (format: r1 c1 r2 c2):")
                while True:
                    try:
                        r1, c1, r2, c2 = map(int, input().split())
                        move = ((r1, c1), (r2, c2))
                        if move in self.get_valid_moves(WHITE):
                            self.apply_move(move)
                            break
                        else:
                            print("Invalid move. Try again.")
                    except:
                        print("Invalid input. Format: r1 c1 r2 c2")
                self.current_player = BLACK
            else:
                print("AI is thinking...")
                _, move = self.minimax(self.board, 3, float('-inf'), float('inf'), True)
                if move:
                    print(f"AI moves: {move[0]} -> {move[1]}")
                    self.apply_move(move)
                self.current_player = WHITE

        self.print_board()
        if not self.get_valid_moves(WHITE):
            print("Game over! AI wins!")
        elif not self.get_valid_moves(BLACK):
            print("Game over! You win!")
        else:
            print("Game ended in a draw.")


if __name__ == '__main__':
    game = Checkers()
    game.play()
