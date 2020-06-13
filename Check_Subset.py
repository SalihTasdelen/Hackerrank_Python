# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    al = int(input())
    aset = set(map(int, input().split()))
    bl = int(input())
    bset = set(map(int, input().split()))
    if aset == bset.intersection(aset):
        print("True")
    else:
        print("False")
