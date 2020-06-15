# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())

for _ in range(t):
    string = input()
    try:
        re.compile(string)
        print("True")
    except re.error:
        print("False")
