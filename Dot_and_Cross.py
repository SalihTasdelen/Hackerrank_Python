import numpy as np
n = int(input())
a_arr = np.empty((n,n), dtype="int32")
b_arr = np.empty((n,n), dtype="int32")
for i in range(n):
    a_arr[i] = list(map(int, input().split()))
for i in range(n):
    b_arr[i] = list(map(int, input().split()))

print(np.dot(a_arr, b_arr))
