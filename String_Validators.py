if __name__ == '__main__':
    s = input()
    validations = list()
    for i in range(5):
        validations.append(False)

    for c in s:
        if c.isalnum():
            validations[0] = True
        if c.isalpha():
            validations[1] = True
        if c.isdigit():
            validations[2] = True
        if c.islower():
            validations[3] = True
        if c.isupper():
            validations[4] = True

    for i in range(5):
        print(validations[i])
