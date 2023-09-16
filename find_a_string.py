def count_substring(string: str, sub_string: str):
    start = 0
    count = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1: return count
        count+=1
        start+=1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)