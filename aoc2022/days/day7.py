import string
from collections import defaultdict


def build_fs(commoutput):
    filesystem = defaultdict(int)
    current_path = []
    for line in commoutput.split("\n"):
        if line[0] == "$":
            line = line.split()
            comm = line[1]
            if comm == "cd":
                if line[2] != "..":
                    current_path.append(line[2])
                else:
                    current_path.pop()
        if line[0] in string.digits:
            size, file = line.split()
            # each file contributes to the total size of all its parent directories
            for i, part in enumerate(current_path):
                if i == 0:
                    filesystem["/"] += int(size)
                else:
                    filesystem["/" + "/".join(current_path[1:i] + [part])] += int(size)

    return filesystem


def sum_hunnit_kays(filesystem):
    hunnits = []
    for path, size in filesystem.items():
        if size <= 100000:
            hunnits.append(path)
    return sum([filesystem[path] for path in hunnits])


TOTAL_DISK_SPACE = 70000000
NEEDED_FOR_UPDATE = 30000000
def find_deletable(filesystem):
    deletable = []
    current_free = TOTAL_DISK_SPACE - filesystem["/"]
    for path, size in filesystem.items():
        if path == "/":
            continue
        after_deleted = current_free + size
        if after_deleted >= NEEDED_FOR_UPDATE:
            deletable.append(size)
    return sorted(deletable)[0]


def answer(data):
    return sum_hunnit_kays(build_fs(data))


def answer_part_two(data):
    return find_deletable(build_fs(data))


if __name__ == "__main__":
    data = open("inputs/day7.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))

