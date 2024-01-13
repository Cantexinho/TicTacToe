import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board_size = 4
        self.game = TicTacToe(self.board_size)

    def test_all_squares_empty_at_start(self):
        self.assertEqual(self.game.num_empty_squares(), self.board_size**2)

    def test_empty_board(self):
        self.assertEqual(self.game.board, [" " for _ in range(self.board_size**2)])
        self.assertEqual(self.game.current_winner, None)

    def test_cannot_move_on_non_empty_square(self):
        self.game.make_move(0, "O")
        self.assertEqual(self.game.board[0], "O")
        self.assertFalse(self.game.make_move(0, "X"))

    def test_make_move(self):
        empty_spaces = self.game.num_empty_squares()
        self.assertTrue(self.game.make_move(0, "X"))
        self.assertEqual(self.game.board[0], "X")
        self.assertEqual(self.game.num_empty_squares(), empty_spaces - 1)

    def test_available_moves(self):
        moves = self.game.available_moves()
        self.assertEqual([i for i in range(self.board_size**2)], moves)

    def test_winner_row(self):
        for i in range(self.board_size - 2):
            self.game.board[i : i + 3] = ["X", "X", "X"]
            self.assertTrue(self.game.check_win_condition("X"))
            self.game.board[i : i + 3] = [" ", " ", " "]

    def test_winner_column(self):
        for i in range(self.board_size - 2):
            self.game.board[i * self.board_size : i * self.board_size + 3] = [
                "X",
                "X",
                "X",
            ]
            self.assertTrue(self.game.check_win_condition("X"))
            self.game.board[i * self.board_size : i * self.board_size + 3] = [
                " ",
                " ",
                " ",
            ]

    def test_winner_diagonal(self):
        for i in range(self.board_size - 2):
            self.game.board[
                i * (self.board_size + 1) : i * (self.board_size + 1) + 3
            ] = ["X", "X", "X"]
            self.assertTrue(self.game.check_win_condition("X"))
            self.game.board[
                i * (self.board_size + 1) : i * (self.board_size + 1) + 3
            ] = [" ", " ", " "]

    def test_winner_other_diagonal(self):
        for i in range(self.board_size - 2):
            self.game.board[
                i * (self.board_size - 1)
                + self.board_size : i * (self.board_size - 1)
                + self.board_size
                + 3
            ] = ["X", "X", "X"]
            self.assertFalse(self.game.check_win_condition("O"))
            self.game.board[
                i * (self.board_size - 1)
                + self.board_size : i * (self.board_size - 1)
                + self.board_size
                + 3
            ] = [" ", " ", " "]

    def test_winner_requires_at_least_three(self):
        self.game.board[0:2] = ["X", "X"]
        self.assertFalse(self.game.check_win_condition("X"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
