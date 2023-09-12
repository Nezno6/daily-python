def swap_case(input_string: str):
    return input_string.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)