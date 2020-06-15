# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    lastdel = 0
    for i in range(len(cubes)):
        if cubes[0] >= cubes[-1]:
            if cubes[0] <= lastdel or lastdel == 0:
                lastdel = cubes.popleft()
        else:
            if cubes[-1] <= lastdel or lastdel == 0:
                lastdel = cubes.pop()
    if len(cubes) > 1:
        print("No")
        continue
    print("Yes")
