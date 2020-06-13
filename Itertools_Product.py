# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

tlist = list(product(alist, blist))
print(" ".join(str(item) for item in tlist))
