import pathlib


def answer(data):
    diagram = data.split("\n")

    beams = {diagram[0].find("S")}
    splits = 0
    for level in diagram:
        splitters = [i for i, char in enumerate(level) if char == "^"]
        for split in splitters:
            try:
                beams.remove(split)
                beams.add(split - 1)
                beams.add(split + 1)
                splits += 1
            except KeyError:
                pass

    return splits

def answer_part_two(data):
    return 0


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day7.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
