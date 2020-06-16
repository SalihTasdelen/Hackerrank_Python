# Enter your code here. Read input from STDIN. Print output to STDOUT
temp = input().split()
n, x = int(temp[0]), int(temp[1])
marks = list()
for _ in range(x):
    marks.append(list(map(float, input().split())))

for x in zip(*marks):
    print(sum(x)/len(x))
