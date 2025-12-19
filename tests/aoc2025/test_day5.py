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
        3-5
        10-14
        16-20
        12-18

        _
    """
    assert answer_part_two(data.strip()) == 14


def test_answer_part_two_more_samples():
    data = """
        3-5
        6-8
        10-14
        16-20
        12-18
        30-42
        22-35

        _
    """
    assert answer_part_two(data.strip()) == 38
