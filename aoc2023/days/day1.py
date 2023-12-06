import pathlib
import re


NUMBER_NAMES = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

FLIPPED_NUMBER_NAMES = {
    "orez": 0,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}


def first_digit(data):
    for char in data:
        if char.isdigit():
            return int(char)


def last_digit(data):
    for char in data[::-1]:
        if char.isdigit():
            return int(char)


def two_digit_numbers(data):
    return int(f"{first_digit(data)}{last_digit(data)}")


def first_digit_or_spelled_out_number(data):
    digit_or_spelled_out = re.search(
        r"(zero|one|two|three|four|five|six|seven|eight|nine|\d)",
        data
    ).group()

    if digit_or_spelled_out.isdigit():
        return int(digit_or_spelled_out)
    else:
        return NUMBER_NAMES[digit_or_spelled_out]


def last_digit_or_spelled_out_number(data):
    digit_or_spelled_out = re.search(
        r"(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)",
        data[::-1]
    ).group()

    if digit_or_spelled_out.isdigit():
        return int(digit_or_spelled_out)
    else:
        return FLIPPED_NUMBER_NAMES[digit_or_spelled_out]


def two_digit_or_spelled_out_numbers(data):
    return int(
        f"{first_digit_or_spelled_out_number(data)}"
        f"{last_digit_or_spelled_out_number(data)}"
    )


def answer(data):
    numbers = []
    for line in data.split("\n"):
        numbers.append(two_digit_numbers(line))
    return sum(numbers)


def answer_part_two(data):
    numbers = []
    for line in data.split("\n"):
        numbers.append(two_digit_or_spelled_out_numbers(line))
    return sum(numbers)


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day1.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
