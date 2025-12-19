from aoc2023.days.day7 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
32T3K 765
    """
    assert answer(data.strip()) == [('32T3K', 765)]


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) is None
