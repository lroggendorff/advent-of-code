import math
import pathlib


def answer(data):
    worksheet = data.split("\n")
    columns = [[] for _ in worksheet[0].split()]

    for row in worksheet:
        for i, column in enumerate(row.split()):
            columns[i].append(column)

    total = 0
    for column in columns:
        operator = column.pop()
        column_value = 0
        if operator == "+":
            column_value = sum([int(c) for c in column])
        else:
            column_value = math.prod([int(c) for c in column])
        total += column_value

    return total


def answer_part_two(data):
    return 0


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day6.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
