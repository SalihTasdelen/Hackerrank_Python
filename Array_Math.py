import numpy as np

temp = list(map(int, input().split()))
n, m = temp[0], temp[1]

a_arr=np.empty((n,m), dtype="int32")
b_arr=np.empty((n,m), dtype="int32")

for i in range(n):
    a_arr[i] = list(map(int, input().split()))
for i in range(n):
    b_arr[i] = list(map(int, input().split()))

print(a_arr + b_arr)
print(a_arr - b_arr)
print(a_arr * b_arr)
print(a_arr // b_arr)
print(a_arr % b_arr)
print(a_arr ** b_arr)
