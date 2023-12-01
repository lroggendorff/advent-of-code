def answer(data):
    reached = 0
    for i, char in enumerate(data):
        maybe = data[i:i+4]
        yep = len(set(maybe)) == len(maybe)
        if yep:
            reached = i + 4
            break
    return reached


def answer_part_two(data):
    reached = 0
    for i, char in enumerate(data):
        maybe = data[i:i+14]
        yep = len(set(maybe)) == len(maybe)
        if yep:
            reached = i + 14
            break
    return reached


if __name__ == "__main__":
    data = open("inputs/day6.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))

