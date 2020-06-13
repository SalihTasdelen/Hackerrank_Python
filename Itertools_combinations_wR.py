# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
temp = list(input().split())
word = list(n for n in temp[0])
word.sort()
word = combinations_with_replacement(word, int(temp[1]))
for element in word:
    print("".join(element))
