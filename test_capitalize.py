from capitalize import capitalize

def test_capitalize():
    assert capitalize("alison heck") == "Alison Heck"
    assert capitalize("chris alan") == "Chris Alan"
    assert capitalize("aLison heck") == "Alison Heck"
    assert capitalize("chris alAn") == "Chris Alan"
    assert capitalize("12abc") == "12abc"
    assert capitalize("12abc abc") == "12abc Abc"
    assert capitalize("12cc      abc") == "12cc      Abc"
    assert capitalize("12cc      abc  ") == "12cc      Abc  "
    assert capitalize("   12cc      abc") == "   12cc      Abc"