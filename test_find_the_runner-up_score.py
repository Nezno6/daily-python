import pytest
from find_the_runner_up_score import SecondMaxValueCouldNotBeFoundError, find_the_second_maximum_value

def test_find_the_second_maximum_value():
    assert(find_the_second_maximum_value([2,3,6,6,5])) == 5
    assert(find_the_second_maximum_value([8,3,6,6,5])) == 6
    assert(find_the_second_maximum_value([2,3])) == 2
    assert(find_the_second_maximum_value([-2,-3,-6,-6,-5])) == -3
    assert(find_the_second_maximum_value([-2,-3,-6,-6,0])) == -2
    assert(find_the_second_maximum_value([2,3,-6,-6,5])) == 3
    assert(find_the_second_maximum_value([2,-3,0,-6,-5])) == 0

def test_could_not_find_the_second_maximum_value():
    with pytest.raises(SecondMaxValueCouldNotBeFoundError):
        find_the_second_maximum_value([2,2,2,2,2])
        