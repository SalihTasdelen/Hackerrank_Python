n = int(input())
s = set(map(int, input().split()))
k = int(input())

command, var= 0, 0

for i in range(k):
    temp = input().split()
    if len(temp) > 1:
        command, var = temp
    else:
        command = temp[0]
    if command == "remove":
        if int(var) in s:
            s.remove(int(var))
    if command == "discard":
        s.discard(int(var))
    if command == "pop":
        if len(s) > 0:
            s.pop()
print(sum(s))
