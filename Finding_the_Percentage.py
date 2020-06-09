if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avarage = 0
    num_of_marks = len(student_marks.get(query_name))
    for i in range(num_of_marks):
        avarage += student_marks.get(query_name)[i] / num_of_marks
    print("%.2f" % avarage)
