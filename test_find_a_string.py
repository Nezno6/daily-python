from find_a_string import count_substring

def test_find_a_string():
    assert count_substring("ABCDCDC", "CDC") == 2
    assert count_substring("     cat   cat  ca   tcat", "cat") == 3
    assert count_substring("ABCDCDCDCDCDC", "CDC") == 5