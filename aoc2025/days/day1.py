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
    commands = [{ "direction": c[0], "amount": int(c[1:]) } for c in data.split("\n")]

    code = 0
    value = 50
    for command in commands:
        direction = command["direction"]
        amount = command["amount"]

        if direction == "L":
            if value == 0:
                code -= 1  ## Starting a rotation at zero doesn't count
            if value - amount <= 0:
                code += -1 * (value - amount) // 100 + 1
            value = (value - amount) % 100
        else:
            if value + amount >= 100:
                code += (value + amount) // 100
            value = (value + amount) % 100

    return code


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day1.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
