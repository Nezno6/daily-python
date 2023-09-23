def add_nxt_letter_as_a_neighbor_of_prv(square,i,j):
    new_square = square[:]
    nxt = chr(ord(new_square[i][j])+1)
    if new_square[i][j-1] == '-': new_square[i][j-1]=nxt
    if new_square[i][j+1] == '-': new_square[i][j+1]=nxt
    if new_square[i-1][j] == '-': new_square[i-1][j]=nxt
    if new_square[i+1][j] == '-': new_square[i+1][j]=nxt
    return new_square

def for_each_cell_add_nxt_letter_as_a_neighbor_of_prv(square,next_letter_idx):
    new_square = square[:]
    size = len(new_square)
    for i in range(0,size):
      for j in range(0,size):
        if new_square[i][j]=='abcdefghijklmnopqrstuvwxyz'[next_letter_idx]:
          add_nxt_letter_as_a_neighbor_of_prv(new_square,i,j)
    return new_square

def create_empty_square(size):
    return [['-' for _ in range(size)] for _ in range(size)]

def draw_a_in_the_middle(square):
    new_square = square[:]
    size=len(new_square)
    new_square[size//2][size//2]='a'
    return new_square

def create_square(square):
    new_square = []
    for row in square:
        new_square.append('-'.join(row))
    return new_square

def draw_alphabet_square(max_letter):
    size=max_letter*2-1
    new_square = draw_a_in_the_middle(create_empty_square(size))
    for letter_idx in range(0,max_letter-1):
       for_each_cell_add_nxt_letter_as_a_neighbor_of_prv(new_square,letter_idx)
    return create_square(new_square)

def print_rangoli(size):
    print("\n".join(draw_alphabet_square(size)))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)