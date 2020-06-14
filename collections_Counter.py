# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
slist = list(map(int, input().split()))
cn = int(input())

customers = list()
for _ in range(cn):
    customers.append(list(map(int, input().split())))

stock = dict(Counter(slist))

earned = 0
for customer in customers:
    if stock.get(customer[0], 0) > 0:
        earned += customer[1]
        stock.update({customer[0] : stock.get(customer[0]) - 1})

print(earned)
