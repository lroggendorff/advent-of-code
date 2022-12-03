from days.day2 import (
    answer,
    answer_part_two,
    determine_my_play,
    play_round,
)


def test_play_round():
    assert play_round("A", "X") == 3
    assert play_round("A", "Y") == 6
    assert play_round("A", "Z") == 0
    assert play_round("B", "X") == 0
    assert play_round("B", "Y") == 3
    assert play_round("B", "Z") == 6
    assert play_round("C", "X") == 6
    assert play_round("C", "Y") == 0
    assert play_round("C", "Z") == 3


def test_determine_my_play():
    assert determine_my_play("A", "X") == "Z"
    assert determine_my_play("A", "Y") == "X"
    assert determine_my_play("A", "Z") == "Y"
    assert determine_my_play("B", "X") == "X"
    assert determine_my_play("B", "Y") == "Y"
    assert determine_my_play("B", "Z") == "Z"
    assert determine_my_play("C", "X") == "Y"
    assert determine_my_play("C", "Y") == "Z"
    assert determine_my_play("C", "Z") == "X"


def test_answer():
    data = """
A Y
B X
C Z
B Z
"""
    assert answer(data.strip()) == 24


def test_answer_part_two():
    data = """
A Y
B X
C Z
B Z
"""
    assert answer_part_two(data.strip()) == 21
