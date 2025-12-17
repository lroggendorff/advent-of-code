from aoc2025.days.day6 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
    """
    assert answer(data.strip()) == 4277556


def test_answer_part_two():
    data = """

    """
    assert answer_part_two(data.strip()) == 0
