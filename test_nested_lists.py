from nested_lists import return_name_of_students_with_second_lowest_grade

def test_nested_list():
    assert return_name_of_students_with_second_lowest_grade(
"""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39""") == """Berry
Harry"""
    assert return_name_of_students_with_second_lowest_grade(
"""3
Chi
20.0
Beta
50.0
Alpha
50.0""") == """Alpha
Beta"""