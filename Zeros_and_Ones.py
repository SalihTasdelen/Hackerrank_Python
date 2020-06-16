import numpy as np

dimtup = tuple(map(int, input().split()))

zeroarr = np.zeros(dimtup, dtype="int8")
onearr = np.ones(dimtup, dtype="int8")
print(zeroarr)
print(onearr)
