import string
from collections import defaultdict, deque


def display_stacks(stacks):
    for i in sorted(stacks.keys()):
        print(f"{i}: {list(stacks[i])}")


def parse_stacks(diagram):
    stacks = defaultdict(deque)
    for line in diagram.split("\n"):
        line = "  " + line
        if line == "" or "[" not in line:
            continue
        column = 0
        for i, char in enumerate(line):
            if char not in " []":
                column = (i + 1) // 4
                stacks[column].appendleft(char)
    return stacks


def parse_instructions(insts):
    instructions = []
    for instruction in insts.split("\n"):
        moves = []
        for word in instruction.split():
            try:
                moves.append(int(word))
            except:
                pass
        instructions.append(moves)
    return instructions


def crate_mover_9000(stacks, instructions):
    moves = parse_instructions(instructions)
    for move in moves:
        for i in range(0, move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    return stacks


def crate_mover_9001(stacks, instructions):
    moves = parse_instructions(instructions)
    for move in moves:
        ordered = []
        for i in range(0, move[0]):
            ordered.insert(0, stacks[move[1]].pop())
        stacks[move[2]].extend(ordered)
    return stacks


def skim_the_top(stacks):
    tops = ""
    for column in sorted(stacks.keys()):
        tops += stacks[column].pop()
    return tops


def answer(data):
    data = data.split("\n\n")
    diagram = data[0]
    instructions = data[1]
    stacks = parse_stacks(diagram)
    return skim_the_top(crate_mover_9000(stacks, instructions))


def answer_part_two(data):
    data = data.split("\n\n")
    diagram = data[0]
    instructions = data[1]
    stacks = parse_stacks(diagram)
    return skim_the_top(crate_mover_9001(stacks, instructions))


if __name__ == "__main__":
    data = open("inputs/day5.txt").read()
    print(answer(data.rstrip()))
    print(answer_part_two(data.rstrip()))
