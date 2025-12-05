from aoc2025.days.day1 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
    """
    assert answer(data.strip()) == 3


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) == 0
