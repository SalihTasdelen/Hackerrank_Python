import numpy as np
temp = list(input().split())
n, m = int(temp[0]), int(temp[1])

arr = np.empty((n,m), dtype="int32")

for i in range(n):
    arr[i] = list(map(int, input().split()))
print(np.transpose(arr))
print(arr.flatten())
