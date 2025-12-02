import pathlib


def answer(data):
    return data


def answer_part_two(data):
    pass


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day1.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
