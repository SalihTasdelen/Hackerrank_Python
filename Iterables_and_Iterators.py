# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
alist = input().split()
k = int(input())

clist = list(combinations([n for n in range(len(alist))], k))

pos = 0
for tup in clist:
    for item in tup:
        if alist[item]=="a":
            pos += 1
            break

print(pos/len(clist))
