from no_idea import calc_happiness

def test_calc_happiness():
    assert calc_happiness([1,5,3],{3,1},{5,7}) == 1