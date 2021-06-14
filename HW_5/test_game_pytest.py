import pytest
from game import TicTacToe

game = TicTacToe()

def setup_module():
    game.board[4] = "X"
    game.board[6] = "O"


def test_available_moves():
    assert (4 not in game.available_moves())
    assert (6 not in game.available_moves())
    assert (5 in game.available_moves())
    assert (3 in game.available_moves())


def test_make_move():
    assert not (game.make_move(4, "X"))
    assert (game.make_move(5, "X"))
    assert not (game.make_move(6, "O"))
    assert (game.make_move(7, "O"))
    assert (game.board[1] == " ")
    assert (game.board[7] != " ")
    assert (game.board[5] != " ")


def test_make_move_negative_case():
    with pytest.raises(IndexError):
        assert game.make_move(10, "X")
        assert game.make_move(9, "X")
        assert game.make_move(6, "X")
        assert game.make_move(4, "O")
        assert game.make_move(2, "O")
        assert game.make_move(1, "O")
