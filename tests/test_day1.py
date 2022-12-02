from days.day1 import answer


def test_answer():
    data = """
1
1
1
1

1
1
1
    """
    assert answer(data.strip()) == 4
