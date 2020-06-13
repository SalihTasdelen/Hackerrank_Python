# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = (input().split())
arr = list(map(int, input().split()))
aset = set(map(int, input().split()))
bset = set(map(int, input().split()))

happiness = 0
for element in arr:
    if element in aset:
        happiness+=1
    elif element in bset:
        happiness-=1
print(happiness)
