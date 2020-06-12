# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
cstamps = set()
for i in range(n):
    cstamps.add(input())
print(len(cstamps))
