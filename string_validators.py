def has_any_char_alphanumeric(string: str):
    return any(char.isalnum() for char in string)

def has_any_char_alphabetical(string: str):
    return any(char.isalpha() for char in string)

def has_any_char_digits(string: str):
    return any(char.isdigit() for char in string)

def has_any_char_lowercase(string: str):
    return any(char.islower() for char in string)

def has_any_char_uppercase(string: str):
    return any(char.isupper() for char in string)

def string_validators(string: str):
    print(has_any_char_alphanumeric(string), 
    has_any_char_alphabetical(string),
    has_any_char_digits(string),
    has_any_char_lowercase(string),
    has_any_char_uppercase(string), sep = "\n")
        
if __name__ == '__main__':
    string_validators(input())