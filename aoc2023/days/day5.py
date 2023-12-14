import pathlib


def answer(data):
    locations = []
    seeds = [int(seed) for seed in data.split("\n")[0].split(":")[1].split(" ") if seed.isdigit()]
    maps = data.split("\n\n")[1:]
    for seed in seeds:
        needle = seed
        for m in maps:
            ranges = m.split("\n")[1:]
            for r in ranges:
                splitsies = r.split(" ")
                source_start = int(splitsies[1])
                dest_start = int(splitsies[0])
                length = int(splitsies[2])
                if source_start <= needle < source_start + length:
                    if source_start > dest_start:
                        offset = source_start - dest_start
                        needle = needle - offset
                    if source_start < dest_start:
                        offset = dest_start - source_start
                        needle = needle + offset
                    break
        locations.append(needle)
    return min(locations)


def answer_part_two(data):
    pass


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day5.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
