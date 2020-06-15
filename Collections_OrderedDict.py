# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
stock = OrderedDict()
for _ in range(int(input())):
    temp = input().split()
    if len(temp) > 2:
        if temp[0]+" "+temp[1] in stock.keys():
            stock[temp[0]+" "+temp[1]] += int(temp[-1])
            continue
        stock[temp[0]+" "+temp[1]] = int(temp[-1])
    else:
        if temp[0] in stock.keys():
            stock[temp[0]] += int(temp[-1])
            continue
        stock[temp[0]] = int(temp[-1])

for i in range(len(stock)):
    print(list(stock.keys())[i], list(stock.values())[i])
