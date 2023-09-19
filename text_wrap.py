import textwrap

def wrap_text(string: str, length: int):
    return textwrap.wrap(string,length)

def fill_text(string: str, length: int):
    return textwrap.fill(string,length)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap_text(string, max_width)
    print(result)