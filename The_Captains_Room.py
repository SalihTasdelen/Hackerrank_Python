# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rlist = list(map(int, input().split()))
rlist.sort()

for i in range(0, len(rlist), k):
    if i + 1 == len(rlist):
        print(rlist[i])
    elif rlist[i] != rlist[i+1]:
        print(rlist[i])
        break
