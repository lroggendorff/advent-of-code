from aoc2023.days.day4 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
Card 163: 99 57 56  2 37 85 29 60 88 64 | 77 11 47 80 67 76 62 98 50 70 21 45 95 18 68 79 14 90 46 43 19 27 25  7 71
    """
    assert answer(data.strip()) == 13


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) is None
