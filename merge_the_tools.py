def merge_the_tools(string: str, chunk_size: int):
    return [''.join(dict.fromkeys(string[i:i+chunk_size])) for i in range(0, len(string), chunk_size)]
    


if __name__ == '__main__':
    string, chunk_size = input(), int(input())
    merge_the_tools(string, chunk_size)