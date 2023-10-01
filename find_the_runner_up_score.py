class MyProjectError(Exception):
    """Exception class from which every exception in this library will derive.
         It enables other projects using this library to catch all errors coming
         from the library with a single "except" statement
    """
    pass

class SecondMaxValueCouldNotBeFoundError(MyProjectError):
    """A specific error"""
    pass

def find_the_second_maximum_value(arr_of_result):
    list_of_unique_result = sorted(list(set(arr_of_result)))
    if len(list_of_unique_result) < 2:
        raise SecondMaxValueCouldNotBeFoundError("value could not be found")
    return list_of_unique_result[-2]

if __name__ == '__main__':
    n = int(input())
    arr_of_result = list(map(int, input().split()))
    print(find_the_second_maximum_value(arr_of_result))