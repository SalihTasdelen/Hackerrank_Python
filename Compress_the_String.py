# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
alist = list(n for n in input())
blist=list()
for x, g in groupby(alist):
    blist.append([len(list(g)), int(x)])

print(" ".join(str(tuple(n)) for n in blist))
