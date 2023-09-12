def swap_case(input_string: str):
    new_string = ""
    for c in input_string:
        if c == c.lower():
            new_string = new_string + c.upper()
        else:
            new_string = new_string + c.lower()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)