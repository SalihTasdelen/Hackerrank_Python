def print_rangoli(size):
    # your code goes here
    p_list = list()
    ascnum = 96 + size
    width = size*2 -1
    p_list.append(chr(ascnum))
    for i in range(width):
        if 0 < i < size:
            p_list.insert(i, "-" + chr(ascnum - 1))
            p_list.insert(i + 1, "-" + chr(ascnum))
            ascnum-=1
        elif size <= i:
            del p_list[size*2 - i -1]
            del p_list[size*2 - i -1]
        print("".join(p_list).center(width*2 -1, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
