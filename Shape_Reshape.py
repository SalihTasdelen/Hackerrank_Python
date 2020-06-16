import numpy as np

arr = np.array([int(n) for n in input().split()])
reshapedarr = np.reshape(arr, (3,3))
print(reshapedarr)
