from aoc2023.days.day1 import (
    answer,
    answer_part_two,
    first_digit,
    first_digit_or_spelled_out_number,
    last_digit,
    last_digit_or_spelled_out_number,
)


def test_first_digit():
    data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    assert first_digit(data[0]) == 1
    assert first_digit(data[1]) == 3
    assert first_digit(data[2]) == 1
    assert first_digit(data[3]) == 7


def test_last_digit():
    data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    assert last_digit(data[0]) == 2
    assert last_digit(data[1]) == 8
    assert last_digit(data[2]) == 5
    assert last_digit(data[3]) == 7


def test_first_digit_or_spelled_out_number():
    data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "twone",
        "oneight",
    ]

    assert first_digit_or_spelled_out_number(data[0]) == 2
    assert first_digit_or_spelled_out_number(data[1]) == 8
    assert first_digit_or_spelled_out_number(data[2]) == 1
    assert first_digit_or_spelled_out_number(data[3]) == 2
    assert first_digit_or_spelled_out_number(data[4]) == 4
    assert first_digit_or_spelled_out_number(data[5]) == 1
    assert first_digit_or_spelled_out_number(data[6]) == 7
    assert first_digit_or_spelled_out_number(data[7]) == 2
    assert first_digit_or_spelled_out_number(data[8]) == 1


def test_last_digit_or_spelled_out_number():
    data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "twone",
        "oneight",
    ]

    assert last_digit_or_spelled_out_number(data[0]) == 9
    assert last_digit_or_spelled_out_number(data[1]) == 3
    assert last_digit_or_spelled_out_number(data[2]) == 3
    assert last_digit_or_spelled_out_number(data[3]) == 4
    assert last_digit_or_spelled_out_number(data[4]) == 2
    assert last_digit_or_spelled_out_number(data[5]) == 4
    assert last_digit_or_spelled_out_number(data[6]) == 6
    assert last_digit_or_spelled_out_number(data[7]) == 1
    assert last_digit_or_spelled_out_number(data[8]) == 8


def test_answer():
    data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
    """
    assert answer(data.strip()) == 142


def test_answer_part_two():
    data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
    """
    assert answer_part_two(data.strip()) == 281
