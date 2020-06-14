# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
temp = list(map(int, input().split()))
k, m = temp[0], temp[1]
masterlist = list()
for _ in range(k):
    masterlist.append(list(map(int, input().split()))[1:])

comlist = product(*masterlist)

mx, temp = 0, 0
for comb in comlist:
    for el in comb:
        temp+= el**2
    temp%=m
    if mx < temp:
        mx = temp
    temp = 0
print(mx)

