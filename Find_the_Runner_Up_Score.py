def sort_arr(arr):
    temp = 0
    moved = True
    while moved :
        moved = False
        for i in range(len(arr)):
            if i == len(arr) - 1: continue
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                moved = True
                continue

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    sort_arr(arr)
    for i in range(len(arr) - 1, -1, -1):
        if i - 1 < 0 : break
        if arr[i - 1] < arr[i]:
            print(arr[i - 1])
            break
