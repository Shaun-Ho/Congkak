import pytest

from congkak.moves.containers import PlayerMove
from congkak.board.containers import BoardState, PlayerNumber

def test_player_move()->PlayerMove:
    valid_move = PlayerMove(
        player_number=PlayerNumber.ONE,
        pit_number=0
    )
    assert valid_move.pit_number == 0
    with pytest.raises(ValueError):
        invalid_move = PlayerMove(
            player_number=PlayerNumber.ONE,
            pit_number=7
        )