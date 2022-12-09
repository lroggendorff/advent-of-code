def populate_grove(lines):
    grove = []
    for row, trees in enumerate(lines):
        grove.append([])
        for column, tree in enumerate(trees):
            grove[row].append(int(tree))
    return grove


def visible_north(tree, grove):
    if tree[0] == 0:
        return True
    height = grove[tree[0]][tree[1]]
    for row in grove[:tree[0]]:
        if row[tree[1]] >= height:
            return False
    return True


def visible_east(tree, grove):
    if tree[1] == len(grove[0]) - 1:
        return True
    height = grove[tree[0]][tree[1]]
    row = grove[tree[0]]
    for spruce in row[tree[1] + 1:]:
        if spruce >= height:
            return False
    return True


def visible_south(tree, grove):
    if tree[0] == len(grove) - 1:
        return True
    height = grove[tree[0]][tree[1]]
    for row in grove[tree[0] + 1:]:
        if row[tree[1]] >= height:
            return False
    return True


def visible_west(tree, grove):
    if tree[1] == 0:
        return True
    height = grove[tree[0]][tree[1]]
    row = grove[tree[0]]
    for holly in row[:tree[1]]:
        if holly >= height:
            return False
    return True


def answer(data):
    exposed = 0
    grove = populate_grove(data.split("\n"))
    rows = len(grove)
    columns = len(grove[0])
    for row in range(rows):
        for column in range(columns):
            if any([
                visible_north((row, column), grove),
                visible_east((row, column), grove),
                visible_south((row, column), grove),
                visible_west((row, column), grove),
            ]):
                exposed += 1
    return exposed


def calculate_scenics_north(tree, grove):
    if tree[0] == 0:
        return 0
    height = grove[tree[0]][tree[1]]
    distance = 0
    for row in grove[:tree[0]]:
        if row[tree[1]] < height:
            distance += 1
        elif row[tree[1]] == height:
            distance += 1
            break
    return distance


def calculate_scenics_east(tree, grove):
    if tree[1] == len(grove[0]) - 1:
        return 0
    height = grove[tree[0]][tree[1]]
    row = grove[tree[0]]
    distance = 0
    for spruce in row[tree[1] + 1:]:
        if spruce < height:
            distance += 1
        elif spruce == height:
            distance += 1
            break
    return distance


def calculate_scenics_south(tree, grove):
    if tree[0] == len(grove) - 1:
        return 0
    height = grove[tree[0]][tree[1]]
    distance = 0
    for row in grove[tree[0] + 1:]:
        if row[tree[1]] < height:
            distance += 1
        elif row[tree[1]] == height:
            distance += 1
            break
    return distance


def calculate_scenics_west(tree, grove):
    if tree[1] == 0:
        return 0
    height = grove[tree[0]][tree[1]]
    row = grove[tree[0]]
    distance = 0
    for holly in row[:tree[1]]:
        if holly < height:
            distance += 1
        elif holly == height:
            distance += 1
            break
    return distance

def answer_part_two(data):
    scenic_score = 0
    grove = populate_grove(data.split("\n"))
    rows = len(grove)
    columns = len(grove[0])
    for row in range(rows):
        for column in range(columns):
            north_score = calculate_scenics_north((row, column), grove)
            east_score = calculate_scenics_east((row, column), grove)
            south_score = calculate_scenics_south((row, column), grove)
            west_score = calculate_scenics_west((row, column), grove)
            new_score = north_score * east_score * south_score * west_score
            if new_score > scenic_score:
                scenic_score = new_score
    return scenic_score


if __name__ == "__main__":
    data = open("inputs/day8.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))

