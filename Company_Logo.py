#!/bin/python3
from itertools import groupby

if __name__ == '__main__':
    s = sorted(list(input()))
    ordlist = [(c,len(list(ls))) for c, ls in groupby(s)]
    ordlist = sorted(ordlist, key= lambda t: t[1], reverse=True)
    for item in ordlist[:3]:
        print(" ".join(str(n) for n in item))
