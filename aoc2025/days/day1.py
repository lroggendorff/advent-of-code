import pathlib


def answer(data):
    commands = [{ "direction": c[0], "amount": int(c[1:]) } for c in data.split("\n")]

    code = 0
    value = 50
    for command in commands:
        direction = command["direction"]
        amount = command["amount"]

        if direction == "L":
            value = (value - amount) % 100
        else:
            value = (value + amount) % 100

        if value == 0:
            code += 1

    return code


def answer_part_two(data):
    return 0


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day1.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
