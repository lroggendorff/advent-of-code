from aoc2023.days.day7 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
    """
    assert answer(data.strip()) == 6440


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) is None
