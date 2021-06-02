import pytest
from game import TicTacToe

@pytest.fixture(scope="module")
def setup_():
    game = TicTacToe()
    game.board[4] = "X"
    return game


def test_available_moves(setup_):
    assert (4 not in setup_.available_moves())
    

def test_make_move(setup_):
    assert not (setup_.make_move(4, "X"))
    assert (setup_.make_move(5, "X"))
    assert (setup_.board[5] != ' ')
