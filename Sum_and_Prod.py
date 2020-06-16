import numpy as np
temp = list(map(int, input().split()))
n, m = temp[0], temp[1]
arr = np.empty((n,m), dtype="int32")
for i in range(n):
    arr[i] = list(map(int, input().split()))

print(np.prod(np.sum(arr, axis=0)))

