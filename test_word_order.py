from word_order import word_order

def test_word_order():
    assert word_order(["bcdef","abcdefg","bcde","bcdef"]) == "3\n2 1 1" 