from aoc2022.days.day8 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
30373
25512
65332
33549
35390
    """
    assert answer(data.strip()) == 21

def test_answer_part_two():
    data = """
30373
25512
65332
33549
35390
    """
    assert answer_part_two(data.strip()) == 8
