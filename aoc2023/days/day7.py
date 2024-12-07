import pathlib


def answer(data):
    games = data.split("\n")
    hands_and_bids = [(g.split(" ")[0], int(g.split(" ")[1])) for g in games]
    return hands_and_bids


def answer_part_two(data):
    pass


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day7.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
