def edit_list_of_command(input_string: str):
    list_to_be_edited: list = []
    for line in input_string.splitlines():
        command,*args = line.split()
        args = list(map(int, args))
        execute_command(list_to_be_edited, command, args)
    return list_to_be_edited

def execute_command(list_to_be_edited: list, command: str, args: list):
    if command == "print":
        print(list_to_be_edited)
        return
    method = getattr(list_to_be_edited, command)
    method(*args)

if __name__ == '__main__':
    input_string = ""
    for N in range(int(input())):
        input_string = input_string + input() + "\n"
    edit_list_of_command(input_string)
    

    