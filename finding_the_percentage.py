def get_the_average_of_the_marks_array_for_the_query_student(student_marks: dict, query_name: str):
    query_student_marks = student_marks[query_name]
    return round(sum(query_student_marks)/len(query_student_marks),2)

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    return get_the_average_of_the_marks_array_for_the_query_student(student_marks, query_name)

if __name__ == '__main__':
   print(f"{main():.2f}")