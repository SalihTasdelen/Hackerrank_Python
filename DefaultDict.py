# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

temp = input().split()
m, n = int(temp[0]), int(temp[1])

alist = list()
for _ in range(m):
    alist.append(input())
blist = list()
for _ in range(n):
    blist.append(input())

d = defaultdict(list)

for i in range(len(alist)):
        if alist[i] in blist:
            d[alist[i]].append(i)

for item in blist:
    if item in d.keys():
        print(" ".join(str(n + 1) for n in d.get(item)))
    else:
        print(-1)
