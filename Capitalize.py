#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name_list = list(s)
    name_list[0] = name_list[0].upper()
    for i in range(len(name_list)):
        if name_list[i] == " ":
            name_list[i + 1] = name_list[i + 1].upper()
    return "".join(name_list)     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

