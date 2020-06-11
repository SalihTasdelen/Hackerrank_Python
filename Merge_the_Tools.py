def merge_the_tools(string, k):
    # your code goes here
    temp = ""
    for i in range(0, len(string), k):
        for j in range(k):
            if string[i + j] in temp:
                continue
            else:    
                temp += string[i+j]
        print(temp)
        temp = ""    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
