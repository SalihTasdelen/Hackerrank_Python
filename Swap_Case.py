def swap_case(s):
    temp = list()
    for c in s:
        if c.islower():
            temp.append(c.upper())
        else:
            temp.append(c.lower())    
    temp = "".join(temp)
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
