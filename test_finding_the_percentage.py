from finding_the_percentage import get_the_average_of_the_marks_array_for_the_query_student

def test_finding_the_percentage():
    assert get_the_average_of_the_marks_array_for_the_query_student(
    {"Alpha": [20,30,40], "Beta": [30,50,70]}, "Beta") == 50.0
    assert get_the_average_of_the_marks_array_for_the_query_student(
    {"Krishna": [67,68,69], "Arjun": [70,98,63], "Malika": [52,56,60]}, "Malika") == 56.0
    assert get_the_average_of_the_marks_array_for_the_query_student(
    {"Harsh": [25,26.5,28], "Anurag": [26,28,30]}, "Harsh") == 26.50