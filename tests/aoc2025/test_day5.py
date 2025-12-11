from aoc2025.days.day5 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
        3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32
    """
    assert answer(data.strip()) == 3


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) == 0
