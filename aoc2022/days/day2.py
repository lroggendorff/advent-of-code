ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSS = 0
DRAW = 3

THEIR_PLAYS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

MY_PLAYS = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

WINNERS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

OUTCOMES = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN,
}


def determine_my_play(them, outcome):
    my_play = ROCK
    if OUTCOMES[outcome] == LOSS:
        my_play = WINNERS[THEIR_PLAYS[them]]
    if OUTCOMES[outcome] == DRAW:
        my_play = THEIR_PLAYS[them]
    if OUTCOMES[outcome] == WIN:
        my_play = [k for k, v in WINNERS.items() if v == THEIR_PLAYS[them]][0]
    return [k for k, v in MY_PLAYS.items() if v == my_play][0]


def play_round(them, me):
    if THEIR_PLAYS[them] == MY_PLAYS[me]:
        return DRAW
    if THEIR_PLAYS[them] == WINNERS[MY_PLAYS[me]]:
        return WIN
    if WINNERS[THEIR_PLAYS[them]] == MY_PLAYS[me]:
        return LOSS


def score_round(result, my_play):
    return MY_PLAYS[my_play] + result


def answer(data):
    return sum([
        score_round(
            play_round(
                *rnd.split()
            ),
            rnd.split()[1]
        )
        for rnd in data.split("\n")])


def answer_part_two(data):
    return sum([
        score_round(
            play_round(
                rnd.split()[0],
                determine_my_play(*rnd.split())
            ),
            determine_my_play(*rnd.split())
        )
        for rnd in data.split("\n")])


if __name__ == "__main__":
    data = open("inputs/day2.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))
