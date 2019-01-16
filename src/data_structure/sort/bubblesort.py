def bubble_sort(list):
    if len(list) <= 1:
        return list
    for item in range(len(list) - 1, 0, -1):
        for idx in range(item):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


my_list = [19, 2, 31, 45, 6, 11, 121, 27]
bubble_sort(my_list)
print(my_list)
