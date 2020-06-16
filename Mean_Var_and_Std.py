import numpy as np
#to solve the mismatching spaces in the output 
np.set_printoptions(legacy='1.13')
temp = list(map(int, input().split()))
n, m = temp[0], temp[1]
arr = np.empty((n,m), dtype="int32")
for i in range(n):
    arr[i] = list(map(int, input().split()))
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))
