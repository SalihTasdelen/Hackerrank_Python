# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
doubleque = deque()

for _ in range(int(input())):
    query = input().split()
    if query[0] == "append":
        doubleque.append(query[-1])
    elif query[0] == "popleft":
        doubleque.popleft()
    elif query[0] == "appendleft":
        doubleque.appendleft(query[-1])
    else:
        doubleque.pop()
print(" ".join(list(doubleque)))
