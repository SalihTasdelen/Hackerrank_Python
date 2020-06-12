# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
seta = set(map(int, input().split()))
num_of_lines = int(input())

for i in range(num_of_lines):
    op, length = input().split()
    setb = set(map(int, input().split()))
    if op == "intersection_update":
        seta.intersection_update(setb)
    elif op == "update":
        seta.update(setb)
    elif op == "symmetric_difference_update":
        seta.symmetric_difference_update(setb)
    elif op == "difference_update":
        seta.difference_update(setb)
print(sum(seta))
