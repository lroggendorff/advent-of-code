import pathlib


def answer(data):
    ingredient_ranges, ingredient_ids = data.split("\n\n")
    ingredient_ranges = [r.split("-") for r in ingredient_ranges.split("\n")]
    ingredient_ids = [int(ii) for ii in ingredient_ids.split("\n")]

    fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        for ingredient_range in ingredient_ranges:
            if int(ingredient_range[0]) <= ingredient_id <= int(ingredient_range[1]):
                fresh_ingredients += 1
                break

    return fresh_ingredients


def answer_part_two(data):
    return 0


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day5.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
