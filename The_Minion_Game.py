def minion_game(string):
    # your code goes here
    p_stuart = 0
    p_kevin = 0
    vowels = "AEIOU"
    length = len(string)
    for i in range(length):
        if vowels.count(string[i]):
            p_kevin += length - i
        else:
            p_stuart += length - i
    
    if p_kevin > p_stuart:
        print("Kevin {0}".format(p_kevin))
    elif p_kevin < p_stuart:
        print("Stuart {0}".format(p_stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
