from aoc2022.days.day4 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
    """
    assert answer(data.strip()) == 2

    more_data = """
1-3,6-8
    """
    assert answer(more_data.strip()) == 0


def test_answer_part_two():
    data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
    """
    assert answer_part_two(data.strip()) == 4
