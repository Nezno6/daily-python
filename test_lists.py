from lists import edit_list_of_command

def test_lists():
    input_string = """insert 0 5
insert 1 10
insert 0 6
remove 6
append 9
append 1
sort
pop
reverse"""
    assert edit_list_of_command(input_string) == [9, 5, 1]
    input_string = """append 1
append 2
insert 1 3"""
    assert edit_list_of_command(input_string) == [1, 3, 2]
    input_string = """insert 0 5
insert 1 10
insert 0 6"""
    assert edit_list_of_command(input_string) == [6, 5, 10]
    input_string = """insert 0 5
insert 1 10
insert 0 6
remove 6
append 9
append 1
sort"""
    assert edit_list_of_command(input_string) == [1, 5, 9, 10]