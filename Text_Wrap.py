def wrap(string, max_width):
    ptr = 0
    shift = 0
    temp_list = list(string)
    for i in range(len(temp_list)):
        if ptr + 1 == max_width:
            temp_list.insert(i + shift + 1, "\n")
            shift+=1
            ptr = 0
            continue
        ptr+=1
    res = "".join(temp_list)
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
