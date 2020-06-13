
x=0
y=0
temp = input()
tc =temp[0]

for i in range(1, len(temp)):
    if temp[i] == "-" or temp[i] == "+":
        if temp[1] == - 1:
            x = -int(tc)
        else:
            x = int(tc)
        if temp[i] == "+":
            y = int(temp[i+1:-1])
        else:
            y = -int(temp[i+1:-1])
    else:
        tc+=temp[i]
print(x,y)
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

def atan2(y, x):
    if x > 0:
        return cmath.atan(y / x)
    elif x < 0:
        if y >= 0:
            return cmath.atan(y / x) + cmath.pi
        else:
            return cmath.atan(y / x) - cmath.pi
    else:
        if y > 0:
            return cmath.pi/2
        elif y < 0:
            return -cmath.pi/2
        else:
            return None

x=0
y=0
temp = input()
tc =temp[0]

for i in range(1, len(temp)):
    if temp[i] == "-" or temp[i] == "+":
        if temp[1] == - 1:
            x = -int(tc)
        else:
            x = int(tc)
        if temp[i] == "+":
            y = int(temp[i+1:-1])
        else:
            y = -int(temp[i+1:-1])
    else:
        tc+=temp[i]

r = (cmath.sqrt(x**2 + y**2)).real
p = (atan2(y, x)).real

print(r)
print(p)
