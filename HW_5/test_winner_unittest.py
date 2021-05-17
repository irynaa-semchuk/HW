import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_winner_row(self):
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.game.winner(2, "X"))
        self.game.board = [" ", " ", " ", "X", "X", "X", " ", " ", " "]
        self.assertTrue(self.game.winner(5, "X"))
        self.game.board = [" ", " ", " ", " ", " ", " ", "X", "X", "X"]
        self.assertTrue(self.game.winner(8, "X"))
        self.game.print_board()

    def test_winner_column(self):
        self.game.board = ["X", " ", " ", "X", " ", " ", "X", " ", " "]
        self.assertTrue(self.game.winner(0, "X"))
        self.game.board = [" ", " ", "X", " ", " ", "X", " ", " ", "X"]
        self.assertTrue(self.game.winner(2, "X"))
        self.game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        self.assertTrue(self.game.winner(1, 'X'))
        self.game.print_board()

    def test_winner_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(0, 'X'))
        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(2, 'X'))
        self.game.print_board()

    def test_win_not_won(self):
        self.game.board = ["X", "", "X", " ", " ", " ", "X", " ", " "]
        self.assertFalse(self.game.winner(0, "X"))


if __name__ == "__main__":
    unittest.main()
