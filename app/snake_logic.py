from __future__ import annotations

from dataclasses import dataclass
from random import Random

GRID_WIDTH = 20
GRID_HEIGHT = 20
START_LENGTH = 3

DIRECTIONS: dict[str, tuple[int, int]] = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

OPPOSITES = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left",
}


@dataclass(frozen=True)
class SnakeState:
    snake: tuple[tuple[int, int], ...]
    direction: str
    food: tuple[int, int]
    score: int
    game_over: bool


def random_free_cell(
    snake: tuple[tuple[int, int], ...], rng: Random, width: int, height: int
) -> tuple[int, int]:
    occupied = set(snake)
    candidates = [(x, y) for y in range(height) for x in range(width) if (x, y) not in occupied]
    if not candidates:
        raise ValueError("No free cells available for food placement.")
    return candidates[rng.randrange(len(candidates))]


def create_initial_state(
    rng: Random | None = None, width: int = GRID_WIDTH, height: int = GRID_HEIGHT
) -> SnakeState:
    random_source = rng or Random()
    center_x = width // 2
    center_y = height // 2
    snake = tuple((center_x - idx, center_y) for idx in range(START_LENGTH))
    food = random_free_cell(snake, random_source, width, height)
    return SnakeState(snake=snake, direction="right", food=food, score=0, game_over=False)


def normalize_direction(current: str, requested: str | None) -> str:
    if not requested or requested not in DIRECTIONS:
        return current
    if OPPOSITES[current] == requested:
        return current
    return requested


def step_state(
    state: SnakeState,
    requested_direction: str | None,
    rng: Random | None = None,
    width: int = GRID_WIDTH,
    height: int = GRID_HEIGHT,
) -> SnakeState:
    if state.game_over:
        return state

    random_source = rng or Random()
    direction = normalize_direction(state.direction, requested_direction)
    dx, dy = DIRECTIONS[direction]
    head_x, head_y = state.snake[0]
    next_head = (head_x + dx, head_y + dy)

    out_of_bounds = not (0 <= next_head[0] < width and 0 <= next_head[1] < height)
    ate_food = next_head == state.food
    body_to_check = state.snake if ate_food else state.snake[:-1]
    hit_self = next_head in body_to_check
    if out_of_bounds or hit_self:
        return SnakeState(
            snake=state.snake,
            direction=direction,
            food=state.food,
            score=state.score,
            game_over=True,
        )

    if ate_food:
        next_snake = (next_head,) + state.snake
        try:
            next_food = random_free_cell(next_snake, random_source, width, height)
        except ValueError:
            return SnakeState(
                snake=next_snake,
                direction=direction,
                food=next_head,
                score=state.score + 1,
                game_over=True,
            )
        return SnakeState(
            snake=next_snake,
            direction=direction,
            food=next_food,
            score=state.score + 1,
            game_over=False,
        )

    next_snake = (next_head,) + state.snake[:-1]
    return SnakeState(
        snake=next_snake,
        direction=direction,
        food=state.food,
        score=state.score,
        game_over=False,
    )

