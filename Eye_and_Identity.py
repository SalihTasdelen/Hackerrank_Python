import numpy as np
#to solve the mismatching spaces in the output 
np.set_printoptions(legacy='1.13')
temp = list(map(int, input().split()))
n, m= temp[0], temp[1]

arr = np.eye(n, m, k=0)
print(arr)
