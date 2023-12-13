import pathlib


def answer(data):
    card_scores = []
    for card in data.split("\n"):
        winners = set([num for num in card.split(":")[1].split("|")[0].split(" ") if num.isdigit()])
        possibles = set([num for num in card.split(":")[1].split("|")[1].split(" ") if num.isdigit()])
        points = possibles.intersection(winners)
        if len(points) > 1:
            card_scores.append(1 * 2**(len(points) - 1))
        elif len(points) == 1:
            card_scores.append(1)

    return sum(card_scores)


def answer_part_two(data):
    pass


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day4.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
