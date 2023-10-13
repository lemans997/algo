my_list = [1, 5, 6, 3, 2, 7, 2, 3, 8]


for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)
        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]