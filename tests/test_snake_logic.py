from random import Random

import pytest

from app.snake_logic import SnakeState, create_initial_state, random_free_cell, step_state


def test_create_initial_state_uses_expected_shape():
    state = create_initial_state(Random(7), width=10, height=10)

    assert len(state.snake) == 3
    assert state.direction == "right"
    assert state.score == 0
    assert state.food not in state.snake
    assert not state.game_over


def test_create_initial_state_rejects_boards_that_cannot_fit_starting_snake():
    with pytest.raises(ValueError, match="Board dimensions"):
        create_initial_state(Random(7), width=2, height=2)


def test_step_moves_forward_without_growth():
    state = SnakeState(
        snake=((4, 4), (3, 4), (2, 4)),
        direction="right",
        food=(8, 8),
        score=0,
        game_over=False,
    )

    next_state = step_state(state, requested_direction=None, width=10, height=10)

    assert next_state.snake == ((5, 4), (4, 4), (3, 4))
    assert next_state.score == 0
    assert not next_state.game_over


def test_step_grows_and_increments_score_when_food_eaten():
    state = SnakeState(
        snake=((4, 4), (3, 4), (2, 4)),
        direction="right",
        food=(5, 4),
        score=0,
        game_over=False,
    )

    next_state = step_state(state, requested_direction="right", rng=Random(2), width=10, height=10)

    assert len(next_state.snake) == 4
    assert next_state.snake[0] == (5, 4)
    assert next_state.score == 1
    assert next_state.food not in next_state.snake


def test_step_detects_wall_collision():
    state = SnakeState(
        snake=((0, 0), (1, 0), (2, 0)),
        direction="left",
        food=(9, 9),
        score=0,
        game_over=False,
    )

    next_state = step_state(state, requested_direction="left", width=10, height=10)

    assert next_state.game_over
    assert next_state.snake == state.snake


def test_step_detects_self_collision():
    state = SnakeState(
        snake=((2, 2), (2, 3), (1, 3), (1, 2)),
        direction="up",
        food=(1, 2),
        score=3,
        game_over=False,
    )

    next_state = step_state(state, requested_direction="left", width=6, height=6)

    assert next_state.game_over
    assert next_state.score == 3


def test_random_free_cell_raises_when_board_is_full():
    with pytest.raises(ValueError, match="No free cells"):
        random_free_cell(((0, 0),), Random(1), width=1, height=1)


def test_step_handles_full_board_after_eating_food():
    state = SnakeState(
        snake=((1, 0), (0, 0), (0, 1)),
        direction="right",
        food=(1, 1),
        score=3,
        game_over=False,
    )

    next_state = step_state(state, requested_direction="down", rng=Random(1), width=2, height=2)

    assert next_state.game_over
    assert next_state.score == 4
    assert len(next_state.snake) == 4
    assert next_state.food is None
