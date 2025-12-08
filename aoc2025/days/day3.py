import pathlib


def answer(data):
    banks = [b.strip() for b in data.split("\n")]
    high_joltage = []
    for bank in banks:
        first_digit = 0
        second_digit = 0
        found_first = 0

        for i, d in enumerate(bank[:-1]):
            if int(d) > first_digit:
                found_first = i
                first_digit = int(d)
        for d in bank[found_first + 1:]:
            if int(d) > second_digit:
                second_digit = int(d)
        high_joltage.append(int(f"{first_digit}{second_digit}"))

    return sum(high_joltage)

def answer_part_two(data):
    return 0


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day3.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
