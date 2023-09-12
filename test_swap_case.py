from swap_case import swap_case

def test_swap_case():
    assert swap_case("Www.HackerRank.com") == "wWW.hACKERrANK.COM"
    assert swap_case("Pythonist 2") == "pYTHONIST 2"
    assert swap_case("HackerRank.com") == "hACKERrANK.COM"
    assert swap_case("presents") == "PRESENTS"