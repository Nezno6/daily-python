def count_substring(string: str, sub_string: str):
    count = 0
    for i in range(0, len(string)):
        if string[i:len(sub_string)+i].find(sub_string)==0:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)