import pytest
from game import TicTacToe

'''def setup_class(cls):
    cls.game = TicTacToe()
    cls.game.board[4] = "X"'''


def setup():
    global game
    game = TicTacToe()
    game.board[4] = "X"
    return game


def test_available_moves():
    assert (4 not in setup().available_moves())


def test_make_move():
    assert not (setup().make_move(4, "X"))
    assert (setup().make_move(5, "X"))
    assert (game.board[5] != " ")
