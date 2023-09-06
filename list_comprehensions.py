def get_all_matrixes_which_sum_are_not_equal_n(x: int, y: int, z: int, n: int):
    return [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+k+j != n]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(get_all_matrixes_which_sum_are_not_equal_n(x,y,z,n))
