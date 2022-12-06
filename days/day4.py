def determine_sections(assignment):
    sections = [int(assn) for assn in assignment.split("-")]
    sections[-1] += 1
    return list(range(*sections))


def determine_containment(sections):
    return set(sections[0]).issubset(sections[1]) or set(sections[1]).issubset(sections[0])


def count_containments(assignments):
    return len([o for o in assignments if o])


def answer(data):
    return count_containments(
        [determine_containment(
            [determine_sections(assignment)
            for assignment in assignments]
        ) for assignments in
        [assns.split(",") for assns in data.split("\n")]
        ]
    )


def count_overlaps(assignments):
    return len([o for o in assignments if not o])


def determine_overlap(sections):
    return len(set(sections[0]).intersection(sections[1])) == 0


def answer_part_two(data):
    return count_overlaps(
        [determine_overlap(
            [determine_sections(assignment)
            for assignment in assignments]
        ) for assignments in
        [assns.split(",") for assns in data.split("\n")]
        ]
    )


if __name__ == "__main__":
    data = open("inputs/day4.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))

