def swap_case(input_string: str):
    return ''.join([char_from_string.upper() if char_from_string == char_from_string.lower() else char_from_string.lower() for char_from_string in input_string])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)