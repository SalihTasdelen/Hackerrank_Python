# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_difference(l1, l2):
    templist = list()
    for ite1 in l1:
        if ite1 not in l2:
            templist.append(ite1)
    for ite2 in l2:
        if ite2 not in l1:
            templist.append(ite2)
    templist.sort()
    for it in templist:
        print(it)

m = int(input())
mlist = list(set(map(int, input().split())))
n = int(input())
nlist = list(set(map(int, input().split())))

print_difference(mlist, nlist)
