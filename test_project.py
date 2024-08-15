import pytest
from project import random_starting_position, snake_init, target_init


def test_random_starting_position():
    n1, n2 = random_starting_position()
    assert 40 <= n1 <= 760 and n1 % 20 == 0
    assert 40 <= n2 <= 560 and n2 % 20 == 0


def test_snake_init():
    snake, rect_width, rect_height, yellow_color = snake_init()
    assert isinstance(snake, list)
    assert len(snake) == 1
    assert rect_width == 20
    assert rect_height == 20
    assert yellow_color == (255, 255, 0)
    assert 40 <= snake[0][0] <= 760
    assert 40 <= snake[0][1] <= 560
    assert snake[0][0] % 20 == 0
    assert snake[0][1] % 20 == 0


def test_target_init():
    rect_x, rect_y = random_starting_position()
    target_x, target_y, target_width, target_height, red_color = target_init(
        rect_x, rect_y
    )
    assert 40 <= target_x <= 760
    assert 40 <= target_y <= 560
    assert not (target_x == rect_x and target_y == rect_y)
    assert target_width == 20
    assert target_height == 20
    assert red_color == "red"
