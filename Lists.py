if __name__ == '__main__':  
    com_list = list()
    main_list = list()
    N = int(input())
    for _ in range(N):
        com_list = input().split()
        command = com_list[0]
        if command == "insert":
            main_list.insert(int(com_list[1]), int(com_list[2]))
        elif command == "append":
            main_list.append(int(com_list[1]))
        elif command == "pop":
            main_list.pop()
        elif command == "reverse":
            main_list.reverse()
        elif command == "sort":
            main_list.sort()
        elif command == "remove":
            main_list.remove(int(com_list[1]))
        elif command == "print":
            print(main_list)
        com_list = list()
