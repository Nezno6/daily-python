from athlete_sort import athlete_sort

def test_athlete_sort():
    input_data = """
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1""".strip().splitlines()

    assert athlete_sort(input_data) == """
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12""".strip().splitlines()