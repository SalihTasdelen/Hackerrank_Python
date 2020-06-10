def mutate_string(string, position, character):
    temp = list(string)
    temp[position] = character
    temp = "".join(temp)
    return temp

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
