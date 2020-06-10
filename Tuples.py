from  builtins import hash
if __name__ == '__main__':
    numbers = tuple()
    n = int(input())
    integer_list = map(int, input().split())
    numbers = tuple(integer_list)
    print(hash(numbers))
