from itertools import combinations
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = input().split()
a = list(a)
a.sort()
for i in range(int(b)):
    #take the combinations as a list
    ls = list(combinations(a, i + 1))
    for item in ls:
        ans = "".join(item)
        print(ans)
