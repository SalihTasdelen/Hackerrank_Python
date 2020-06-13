# Enter your code here. Read input from STDIN. Print output to STDOUT
aset = set(map(int, input().split()))
flag = 0
for _ in range(int(input())):
    tset = set(map(int, input().split()))
    if aset.issuperset(tset):
        flag = 1
    else:
        flag = 0
        break
if flag == 1:
    print("True")
else:
    print("False")
