import pathlib
import re


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def answer(data):
    possible_ids = []
    for game in data.split("\n"):
        game_id = re.search(r"Game (\d+)", game).group(1)
        blues = re.findall(r"(\d+) blue", game)
        most_blues = max([int(b) for b in blues])
        greens = re.findall(r"(\d+) green", game)
        most_greens = max([int(b) for b in greens])
        reds = re.findall(r"(\d+) red", game)
        most_reds = max([int(b) for b in reds])
        if (
            most_blues <= MAX_BLUE
            and most_greens <= MAX_GREEN
            and most_reds <= MAX_RED
        ):
            possible_ids.append(int(game_id))
    return sum(possible_ids)


def answer_part_two(data):
    powers = []
    for game in data.split("\n"):
        blues = re.findall(r"(\d+) blue", game)
        most_blues = max([int(b) for b in blues])
        greens = re.findall(r"(\d+) green", game)
        most_greens = max([int(b) for b in greens])
        reds = re.findall(r"(\d+) red", game)
        most_reds = max([int(b) for b in reds])
        powers.append(most_blues * most_greens * most_reds)
    return sum(powers)


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day2.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
