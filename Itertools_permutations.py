# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
alist = input().split()
word = list(c for c in alist[0])
word.sort()
word = list(permutations(word, int(alist[1])))
for item in word:
    print("".join(item))
