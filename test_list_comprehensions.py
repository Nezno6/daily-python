from list_comprehensions import get_all_matrixes_which_sum_are_not_equal_n

def test_get_all_matrixes_which_sum_are_not_equal_n():
    assert get_all_matrixes_which_sum_are_not_equal_n(1,1,2,3) == [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]
    assert get_all_matrixes_which_sum_are_not_equal_n(1,1,1,2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    assert get_all_matrixes_which_sum_are_not_equal_n(2,2,2,2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]