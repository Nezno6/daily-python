from nutrition import get_calories

def test_nutrition():
    assert get_calories("Apple") == 130
    assert get_calories("Banana") == 105
    assert get_calories("Grapes") == 52
    assert get_calories("Orange") == 80
    assert get_calories("Strawberry") == 50
    assert get_calories("Grapefruit") == 60
    assert get_calories("   apple") == 130
    assert get_calories("BanAna") == 105
    assert get_calories("grapeS") == 52
    assert get_calories("oraNGE") == 80
    assert get_calories("Strawberry  ") == 50
    assert get_calories("  Grapefruit") == 60