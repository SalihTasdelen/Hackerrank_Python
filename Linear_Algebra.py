import numpy as np
n = int(input())
arr = np.empty((n,n), dtype="float")
for i in range(n):
    arr[i] = list(map(float, input().split()))
ans = round(np.linalg.det(arr), 2)
print(ans)
