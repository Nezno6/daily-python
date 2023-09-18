def print_number(n):
    number = "";
    for i in range(1,n+1,1):
        number = number+str(i)
    return number
    
if __name__ == '__main__':
    n = int(input())
    print(print_number(n))