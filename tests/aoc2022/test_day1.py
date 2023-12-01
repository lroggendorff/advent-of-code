from aoc2022.days.day1 import (
    answer,
    answer_part_two,
)


def test_answer():
    data = """
1
1
1
1

1
1
1
    """
    assert answer(data.strip()) == 4

def test_answer_part_two():
    data = """
1
1

1
1
1
1

1
1
1

1
1
1
1
1
    """
    assert answer_part_two(data.strip()) == 12
