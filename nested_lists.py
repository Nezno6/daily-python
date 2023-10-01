def parse_input(file: str):
    list_of_students_names = file.splitlines()[1::2]
    list_of_students_grades = [float(grade) for grade in file.splitlines()[2::2]]
    return dict(zip(list_of_students_names, list_of_students_grades))

def get_name_of_students_with_second_lowest_grade(names_to_grades: dict):
    second_lowest_grade = sorted(list(set(names_to_grades.values())))[1]
    names = [name for name, grade in names_to_grades.items() if grade == second_lowest_grade]
    return "\n".join(sorted(names))

def return_name_of_students_with_second_lowest_grade(file: str):
    return get_name_of_students_with_second_lowest_grade(parse_input(file))