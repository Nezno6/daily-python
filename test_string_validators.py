from string_validators import has_any_char_alphanumeric, has_any_char_alphabetical, has_any_char_digits, has_any_char_lowercase, has_any_char_uppercase, string_validators

def test_has_any_char_alphanumeric():
    assert has_any_char_alphanumeric('ab123') == True
    assert has_any_char_alphanumeric('aB123#') == True
    assert has_any_char_alphanumeric('123') == True
    assert has_any_char_alphanumeric('#') == False
    assert has_any_char_alphanumeric('_') == False

def test_has_any_char_alphabetical():
    assert has_any_char_alphabetical('abcD') == True
    assert has_any_char_alphabetical('abcd1') == True
    assert has_any_char_alphabetical('165') == False

def test_has_any_char_digits():
    assert has_any_char_digits('1234') == True
    assert has_any_char_digits('123edsd') == True
    assert has_any_char_digits('edsd') == False

def test_has_any_char_lowercase():
    assert has_any_char_lowercase('abcd123#') == True
    assert has_any_char_lowercase('Abcd123#') == True
    assert has_any_char_lowercase('ABCD123#') == False

def test_has_any_char_uppercase():
    assert has_any_char_uppercase('ABCD123#') == True
    assert has_any_char_uppercase('Abcd123#') == True
    assert has_any_char_uppercase('vbcd123#') == False

def test_string_validators():
    assert has_any_char_alphanumeric('qA2') == True
    assert has_any_char_alphabetical('qA2') == True
    assert has_any_char_digits('qA2') == True
    assert has_any_char_lowercase('qA2') == True
    assert has_any_char_uppercase('qA2') == True