import pathlib


def find_number(x, y, grid):
    number = grid[y][x]
    left_edge = 0
    right_edge = len(grid[y]) - 1
    move = x
    while move >= left_edge:
        move -= 1
        left = grid[y][move]
        if left.isdigit():
            number = left + number
        else:
            break

    move = x
    while move < right_edge:
        move += 1
        right = grid[y][move]
        if right.isdigit():
            number = number + right
        else:
            break

    return number


def check_for_symbol(x, y, grid):
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            try:
                focus = grid[j][i]
                if not focus.isdigit() and focus != ".":
                    return True
            except IndexError:
                continue


def answer(data):
    part_numbers = []
    grid = [list(line) for line in data.strip().split("\n")]
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x].isdigit():
                full_adjacent_number = find_number(x, y, grid)
                if check_for_symbol(x, y, grid):
                    if not len(part_numbers):
                        part_numbers.append(int(full_adjacent_number))

                    if len(part_numbers) and int(full_adjacent_number) != part_numbers[-1]:
                        part_numbers.append(int(full_adjacent_number))

    return sum(part_numbers)


def answer_part_two(data):
    pass


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day3.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
