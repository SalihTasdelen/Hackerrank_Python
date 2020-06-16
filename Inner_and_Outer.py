import numpy as np
a_arr = np.array([int(n) for n in input().split()], dtype="int32")
b_arr = np.array([int(n) for n in input().split()], dtype="int32")
print(np.inner(a_arr, b_arr))
print(np.outer(a_arr, b_arr))
