def get_hash_from_tuple(integer_list: map):
    return hash(tuple(integer_list))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(get_hash_from_tuple(integer_list))