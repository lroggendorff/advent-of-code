from days.day5 import (
    answer,
    answer_part_two,
    parse_instructions,
    parse_stacks,
    crate_mover_9000,
    crate_mover_9001,
)


def test_parse_stacks():
    data = """
            [G] [W]         [Q]
[Z]         [Q] [M]     [J] [F]
[V]         [V] [S] [F] [N] [R]
[T]         [F] [C] [H] [F] [W] [P]
[B] [L]     [L] [J] [C] [V] [D] [V]
[J] [V] [F] [N] [T] [T] [C] [Z] [W]
[G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
[R] [J] [S] [Z] [R] [S] [D] [L] [J]
 1   2   3   4   5   6   7   8   9
    """
    stacks = parse_stacks(data)
    assert list(stacks[1]) == ["R", "G", "J", "B", "T", "V", "Z"]
    assert list(stacks[2]) == ["J", "R", "V", "L"]
    assert list(stacks[3]) == ["S", "Q", "F"]
    assert list(stacks[4]) == ["Z", "H", "N", "L", "F", "V", "Q", "G"]
    assert list(stacks[5]) == ["R", "Q", "T", "J", "C", "S", "M", "W"]
    assert list(stacks[6]) == ["S", "W", "T", "C", "H", "F"]
    assert list(stacks[7]) == ["D", "Z", "C", "V", "F", "N", "J"]
    assert list(stacks[8]) == ["L", "G", "Z", "D", "W", "R", "F", "Q"]
    assert list(stacks[9]) == ["J", "B", "W", "V", "P"]


def test_parse_instructions():
    instructions = """
move 1 from 2 to 1
move 3 from 1 to 3
move 10 from 5 to 7
    """
    assert parse_instructions(instructions.strip()) == [
        [1, 2, 1],
        [3, 1, 3],
        [10, 5, 7],
    ]

def test_crate_mover_9000():
    stacks = {
        1: ["R", "G", "J", "B", "T", "V", "Z"],
        2: ["J", "R", "V", "L"],
        3: ["S", "Q", "F"],
        4: ["Z", "H", "N", "L", "F", "V", "Q", "G"],
        5: ["R", "Q", "T", "J", "C", "S", "M", "W"],
        6: ["S", "W", "T", "C", "H", "F"],
        7: ["D", "Z", "C", "V", "F", "N", "J"],
        8: ["L", "G", "Z", "D", "W", "R", "F", "Q"],
        9: ["J", "B", "W", "V", "P"],
    }
    instructions = """
move 6 from 5 to 7
move 2 from 9 to 1
move 4 from 8 to 6
move 1 from 8 to 1
move 2 from 9 to 1
move 1 from 6 to 1
move 13 from 7 to 8
    """
    assert crate_mover_9000(stacks, instructions.strip()) == {
        1: ["R", "G", "J", "B", "T", "V", "Z", "P", "V", "D", "W", "B", "W"],
        2: ["J", "R", "V", "L"],
        3: ["S", "Q", "F"],
        4: ["Z", "H", "N", "L", "F", "V", "Q", "G"],
        5: ["R", "Q"],
        6: ["S", "W", "T", "C", "H", "F", "Q", "F", "R"],
        7: [],
        8: ["L", "G", "Z", "T", "J", "C", "S", "M", "W", "J", "N", "F", "V", "C", "Z", "D"],
        9: ["J"],
    }

def test_crate_mover_9001():
    stacks = {
        1: ["R", "G", "J", "B", "T", "V", "Z"],
        2: ["J", "R", "V", "L"],
        3: ["S", "Q", "F"],
        4: ["Z", "H", "N", "L", "F", "V", "Q", "G"],
        5: ["R", "Q", "T", "J", "C", "S", "M", "W"],
        6: ["S", "W", "T", "C", "H", "F"],
        7: ["D", "Z", "C", "V", "F", "N", "J"],
        8: ["L", "G", "Z", "D", "W", "R", "F", "Q"],
        9: ["J", "B", "W", "V", "P"],
    }
    instructions = """
move 6 from 5 to 7
move 2 from 9 to 1
move 4 from 8 to 6
move 1 from 8 to 1
move 2 from 9 to 1
move 1 from 6 to 1
move 13 from 7 to 8
    """
    assert crate_mover_9001(stacks, instructions.strip()) == {
        1: ["R", "G", "J", "B", "T", "V", "Z", "V", "P", "D", "B", "W", "Q"],
        2: ["J", "R", "V", "L"],
        3: ["S", "Q", "F"],
        4: ["Z", "H", "N", "L", "F", "V", "Q", "G"],
        5: ["R", "Q"],
        6: ["S", "W", "T", "C", "H", "F", "W", "R", "F"],
        7: [],
        8: ["L", "G", "Z", "D", "Z", "C", "V", "F", "N", "J", "T", "J", "C", "S", "M", "W"],
        9: ["J"],
    }


def test_answer():
    data = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """
    assert answer(data.rstrip()) == "CMZ"


def test_answer_part_two():
    data = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """
    assert answer_part_two(data.rstrip()) == "MCD"
