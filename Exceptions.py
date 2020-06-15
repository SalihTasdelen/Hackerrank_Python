# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    try:
        values = list(map(int, input().split()))
    except ValueError as e:
        print("Error Code: " + str(e))
        continue
    try:
        print(int(values[0] / values[1]))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")#error code from e is not same as what answer wants

