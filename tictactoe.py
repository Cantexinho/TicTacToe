class TicTacToe:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [" " for _ in range(board_size**2)]
        self.current_winner = None

    def print_board(self) -> None:
        for i in range(self.board_size):
            row_start = i * self.board_size
            row_end = (i + 1) * self.board_size

            row = []
            for index in range(row_start, row_end):
                row.append(self.board[index])
            print("| " + " | ".join(row) + " |")

    def available_moves(self) -> list:
        return [i for i, x in enumerate(self.board) if x == " "]

    def empty_squares(self) -> bool:
        return " " in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(" ")

    def make_move(self, square, letter) -> bool:
        if self.board[square] != " ":
            print("Square is occupied")
            return False
        self.board[square] = letter
        if self.check_win_condition(letter):
            self.current_winner = letter
        return True

    def check_win_condition(self, letter) -> bool:
        def _check_rows(letter) -> bool:
            for i in range(self.board_size):
                for j in range(self.board_size - 2):
                    if (
                        self.board[i * self.board_size + j] == letter
                        and self.board[i * self.board_size + j + 1] == letter
                        and self.board[i * self.board_size + j + 2] == letter
                    ):
                        return True
            return False

        def _check_columns(letter) -> bool:
            for i in range(self.board_size):
                for j in range(self.board_size - 2):
                    if (
                        self.board[j * self.board_size + i] == letter
                        and self.board[(j + 1) * self.board_size + i] == letter
                        and self.board[(j + 2) * self.board_size + i] == letter
                    ):
                        return True
            return False

        def _check_diagonal(letter) -> bool:
            for i in range(self.board_size - 2):
                if (
                    self.board[i * (self.board_size + 1)] == letter
                    and self.board[(i + 1) * (self.board_size + 1)] == letter
                    and self.board[(i + 2) * (self.board_size + 1)] == letter
                ):
                    return True
            return False

        def _check_other_diagonal(letter) -> bool:
            for i in range(self.board_size - 2):
                j = i + 2
                if (
                    self.board[j * (self.board_size - 1)] == letter
                    and self.board[(j - 1) * (self.board_size - 1)] == letter
                    and self.board[(j - 2) * (self.board_size - 1)] == letter
                ):
                    return True
            return False

        if self.board.count(letter) >= 3:
            return (
                _check_rows(letter)
                or _check_columns(letter)
                or _check_diagonal(letter)
                or _check_other_diagonal(letter)
            )
        return False
