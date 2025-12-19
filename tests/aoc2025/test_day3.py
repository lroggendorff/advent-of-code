from aoc2025.days.day3 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """
    assert answer(data.strip()) == 357


def test_answer_part_two():
    data = """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """
    assert answer_part_two(data.strip()) == 3121910778619
