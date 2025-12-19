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
    ingredient_ranges, _ = data.split("\n\n")
    ingredient_ranges = [r.split("-") for r in ingredient_ranges.split("\n")]
    ingredient_ranges = [[int(lower), int(upper)] for lower, upper in ingredient_ranges]

    found_unmerged = True

    sorted_ranges = sorted(ingredient_ranges, key=lambda r: r[0])
    maybe_non_overlapping_ranges = []
    while found_unmerged:
        maybe_non_overlapping_ranges = [sorted_ranges[0]]

        found_unmerged = False
        for current_range in sorted_ranges[1:]:
            previous_range = maybe_non_overlapping_ranges[-1]

            if current_range[0] <= previous_range[1]:
                previous_range[1] = max(previous_range[1], current_range[1])
                found_unmerged = True
            else:
                maybe_non_overlapping_ranges.append(current_range)

        sorted_ranges = sorted(maybe_non_overlapping_ranges, key=lambda r: r[0])

    non_overlapping_ranges = maybe_non_overlapping_ranges

    considered_fresh = 0
    for non_overlapping_range in non_overlapping_ranges:
        considered_fresh += int(non_overlapping_range[1]) - int(non_overlapping_range[0]) + 1

    return considered_fresh


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day5.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
