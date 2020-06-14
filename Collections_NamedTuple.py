# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
noc = list(input().split())
Student = namedtuple("Studend", " ".join(n for n in noc))
students = list()
for i in range(n):
    temp = list(input().split())
    students.append(Student(*temp))
avg = 0
for student in students:
    avg += int(student.MARKS)
print(avg / len(students))
