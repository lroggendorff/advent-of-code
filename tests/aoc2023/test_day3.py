from aoc2023.days.day3 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.587
..592.....
......755.
...$.*....
.664.598..
    """
    assert answer(data.strip()) == 4361


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) is None
