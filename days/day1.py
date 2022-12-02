def answer(data):
    return sorted(
        [sum([int(c) for c in chunk.split("\n")]) for chunk in data.split("\n\n")]
    )[-1]


if __name__ == "__main__":
    data = open("data/day1.txt").read()
    print(answer(data.strip()))
