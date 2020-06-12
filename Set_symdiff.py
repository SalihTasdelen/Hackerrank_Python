# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eset = set(map(int, input().split()))
m = int(input())
fset = set(map(int, input().split()))

#inter = eset.intersection(fset)
#sdiff = eset.union(fset)
#sdiff.intersection_update(inter)
sdiff = eset ^ fset 
print(len(sdiff))
