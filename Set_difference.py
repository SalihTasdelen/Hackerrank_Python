# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eset = set(map(int, input().split()))
m = int(input())
fset = set(map(int, input().split()))

eset.difference_update(fset)
print(len(eset))
