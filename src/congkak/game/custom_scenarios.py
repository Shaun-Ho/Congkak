from congkak.board.containers import BoardState, PlayerNumber, Player
from congkak.board.constants import PITS_PER_SIDE
import numpy as np
import enum

__all__ = ["CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING"]


@enum.unique
class CustomGameScenario(enum.Enum):
    NORMAL = enum.auto()
    MOVE = enum.auto()
    FREE_GO = enum.auto()
    STEAL = enum.auto()
    LOSE_GO = enum.auto()
    SCENARIO_1 = enum.auto()


CUSTOM_GAME_INDEX_TO_BOARD_STATE_MAPPING = {
    CustomGameScenario.NORMAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.zeros(PITS_PER_SIDE),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.zeros(PITS_PER_SIDE)
        ),
    ),
    CustomGameScenario.FREE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0 for _ in range(PITS_PER_SIDE - 1)] + [1]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.zeros(PITS_PER_SIDE)
        ),
    ),
    CustomGameScenario.STEAL: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([1] + [0 for _ in range(PITS_PER_SIDE - 1)]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO,
            score=0,
            side=np.array([0] + [0 for _ in range(PITS_PER_SIDE - 2)] + [0]),
        ),
    ),
    CustomGameScenario.LOSE_GO: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.array([0 for _ in range(PITS_PER_SIDE - 1)] + [2]),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.zeros(PITS_PER_SIDE)
        ),
    ),
    CustomGameScenario.SCENARIO_1: BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=0,
            side=np.ones(PITS_PER_SIDE),
        ),
        player_two=Player(
            number=PlayerNumber.TWO, score=0, side=np.ones(PITS_PER_SIDE)
        ),
    ),
}
