import pathlib


def answer(data):
    ranges = [r.split("-") for r in data.split(",")]
    invalid_ids = []
    for rango in ranges:
        for maybe_id in range(int(rango[0]), int(rango[1]) + 1):
            stringy = str(maybe_id)
            halfsies = len(stringy) // 2
            first_half = stringy[:halfsies]
            second_half = stringy[halfsies:]

            if first_half == second_half:
                invalid_ids.append(maybe_id)

    return sum(invalid_ids)


def determine_invalid_id(maybe):
    stringy = str(maybe)
    length = len(stringy)
    for size in range(1, length + 1):
        splits = list(stringy[0 + i:size + i] for i in range(0, length, size))
        if len(splits) == 1:
            continue
        tester = splits[0]
        if all([d == tester for d in splits]):
            return maybe
    return 0


def answer_part_two(data):
    ranges = [r.split("-") for r in data.split(",")]
    invalid_ids = []
    for rango in ranges:
        for maybe_id in range(int(rango[0]), int(rango[1]) + 1):
            invalid_ids.append(determine_invalid_id(maybe_id))

    return sum(invalid_ids)


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day2.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
