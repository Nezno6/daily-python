from merge_the_tools import merge_the_tools

def test_merge_the_tools():
    input_data = """
    AAABCADDE
    3""".strip().splitlines()
    
    assert merge_the_tools(input_data[0],int(input_data[1])) == """
A
BCA
DE""".strip().splitlines()

    input_data = """
    AABCAAADA
    3""".strip().splitlines()

    assert merge_the_tools(input_data[0],int(input_data[1])) == """
AB
CA
AD""".strip().splitlines()