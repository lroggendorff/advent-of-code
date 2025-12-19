from copy import deepcopy
import pathlib


def find_accessible_rolls(matrix):
    east_edge = len(matrix[0]) - 1
    south_edge = len(matrix) - 1

    accessible_rolls = []

    for y, row in enumerate(matrix):
        for x, spot in enumerate(row):
            if spot != "@":
                continue

            surrounding_spots = []

            # corner rolls are always accessible
            if (x == 0 or x == east_edge) and (y == 0 or y == south_edge):
                surrounding_spots.append([])

            # north edge
            elif y == 0:
                # west
                surrounding_spots.append(matrix[y][x - 1])
                # east
                surrounding_spots.append(matrix[y][x + 1])
                # south east
                surrounding_spots.append(matrix[y + 1][x + 1])
                # south
                surrounding_spots.append(matrix[y + 1][x])
                # south west
                surrounding_spots.append(matrix[y + 1][x - 1])

            # east edge
            elif x == east_edge:
                # north west
                surrounding_spots.append(matrix[y - 1][x - 1])
                # north
                surrounding_spots.append(matrix[y - 1][x])
                # south
                surrounding_spots.append(matrix[y + 1][x])
                # south west
                surrounding_spots.append(matrix[y + 1][x - 1])
                # west
                surrounding_spots.append(matrix[y][x - 1])

            # south edge
            elif y == south_edge:
                # north west
                surrounding_spots.append(matrix[y - 1][x - 1])
                # north
                surrounding_spots.append(matrix[y - 1][x])
                # north east
                surrounding_spots.append(matrix[y - 1][x + 1])
                # east
                surrounding_spots.append(matrix[y][x + 1])
                # west
                surrounding_spots.append(matrix[y][x - 1])

            # west edge
            elif x == 0:
                # north
                surrounding_spots.append(matrix[y - 1][x])
                # north east
                surrounding_spots.append(matrix[y - 1][x + 1])
                # east
                surrounding_spots.append(matrix[y][x + 1])
                # south east
                surrounding_spots.append(matrix[y + 1][x + 1])
                # south
                surrounding_spots.append(matrix[y + 1][x])

            else:
                # north west
                surrounding_spots.append(matrix[y - 1][x - 1])
                # north
                surrounding_spots.append(matrix[y - 1][x])
                # north east
                surrounding_spots.append(matrix[y - 1][x + 1])
                # east
                surrounding_spots.append(matrix[y][x + 1])
                # south east
                surrounding_spots.append(matrix[y + 1][x + 1])
                # south
                surrounding_spots.append(matrix[y + 1][x])
                # south west
                surrounding_spots.append(matrix[y + 1][x - 1])
                # west
                surrounding_spots.append(matrix[y][x - 1])

            if len([s for s in surrounding_spots if s == "@"]) < 4:
                accessible_rolls.append((x, y))

    return accessible_rolls


def answer(data):
    matrix = [list(row.strip()) for row in data.split("\n")]
    return len(find_accessible_rolls(matrix))


def answer_part_two(data):
    matrix = [list(row.strip()) for row in data.split("\n")]
    found_accessible_roll_coordinates = find_accessible_rolls(matrix)
    found_accessible_rolls = len(found_accessible_roll_coordinates)
    removed_rolls = 0
    while found_accessible_rolls > 0:
        found_accessible_roll_coordinates = find_accessible_rolls(matrix)
        found_accessible_rolls = len(found_accessible_roll_coordinates)

        next_matrix = deepcopy(matrix)
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                if (x, y) in found_accessible_roll_coordinates:
                    next_matrix[y][x] = "."
                    removed_rolls += 1

        matrix = next_matrix

    return removed_rolls



if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day4.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
