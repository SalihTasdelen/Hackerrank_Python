# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word in words.keys():
        words[word] += 1
        continue
    words[word] = 1

print(len(words))
print(" ".join(str(n) for n in words.values()))
