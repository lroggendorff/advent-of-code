import string


def find_misplaced_item(sack):
    compartment_size = int(len(sack) / 2)
    first_compartment = sack[:compartment_size]
    second_compartment = sack[compartment_size:]
    return set(first_compartment).intersection(set(second_compartment)).pop()


def prioritize_item(item):
    return list(string.ascii_lowercase + string.ascii_uppercase).index(item) + 1


def answer(data):
    return sum([
        prioritize_item(
            find_misplaced_item(
                rucksack
            )
        )
        for rucksack in data.split("\n")
    ])


def prioritize_badges(badges):
    return prioritize_item(badges)


def find_badges(elf_group):
    return set(elf_group[0]).intersection(set(elf_group[1])).intersection(set(elf_group[2])).pop()


def answer_part_two(data):
    def group_elves(rucksacks):
        for i in range(0, len(rucksacks), 3):
            yield rucksacks[i:i + 3]

    return sum([
        prioritize_badges(
            find_badges(
                elf_group
            )
        )
        for elf_group in group_elves(data.split("\n"))
    ])


if __name__ == "__main__":
    data = open("inputs/day3.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
