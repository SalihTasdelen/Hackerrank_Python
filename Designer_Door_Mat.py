# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = input().split()
m = int(m)
n = int(n)
for i in range(m):
    if i < m // 2:
        print((".|." * (i*2 + 1)).center(n, "-"))
    elif i == (m // 2):
        print("WELCOME".center(n, "-"))
    else:
        print((".|." * (m - (i - m // 2)*2)).center(n, "-"))
