def count_substring(string, sub_string):
    ptr = 0
    a = 0
    for i in range(len(string)):
        if i + len(sub_string) < len(string) + 1:
            if string[i:i + len(sub_string)] == sub_string:
                a += 1
        else:
            break
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
