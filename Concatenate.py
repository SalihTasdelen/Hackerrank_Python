import numpy as np

temp = list(map(int, input().split()))
n, m, p= temp[0], temp[1], temp[2]

arr1 = np.empty((n, p), dtype="int32")
arr2 = np.empty((m, p), dtype="int32")

for i in range(n):
    arr1[i] = list(map(int, input().split()))
for i in range(m):
    arr2[i] = list(map(int, input().split()))

print(np.concatenate((arr1, arr2), axis=0))
