def print_formatted(number):
    # your code goes here
    for i in range(number):
        #put i + 1 while right adjusting with the width of bin version
        print('{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}'.format(i + 1, w=len(bin(number))-2))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
