from aoc2022.days.day6 import (
    answer,
    answer_part_two,
)


def test_answer():
    assert answer("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert answer("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert answer("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert answer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert answer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_answer_part_two():
    assert answer_part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert answer_part_two("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert answer_part_two("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert answer_part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert answer_part_two("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
