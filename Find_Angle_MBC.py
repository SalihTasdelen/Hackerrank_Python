# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

#AC = math.sqrt(AB**2 + BC**2)
#BM = AC
#MC**2 = BM**2 + BC**2 +2BM*BC*cos(tetha)

print("{}°".format(round(math.degrees(math.atan2(AB, BC)))))
