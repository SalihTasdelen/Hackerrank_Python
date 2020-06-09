def sort(lst):
    temp = list()
    moved = True
    while moved :
        moved = False
        for i in range(len(lst)):
            if i == len(lst) - 1: continue
            if lst[i][1] > lst[i + 1][1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
                moved = True
                continue

if __name__ == '__main__':
    student_grade = list()
    second_lowest = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grade.append([name, score])
    sort(student_grade)
    for i in range(len(student_grade)):
        if student_grade[i][1] > student_grade[0][1]:
            second_lowest.append(student_grade[i][0])
            for j in range(i, len(student_grade)):
                if j == len(student_grade) - 1: break
                if student_grade[j][1] == student_grade[j + 1][1]:
                    second_lowest.append(student_grade[j + 1][0])
                else:
                    break    
            break
    second_lowest.sort()
    for el in second_lowest:
        print(el)
