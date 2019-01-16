# -*- coding: utf-8 -*-
import timeit


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    middle = len(my_list) // 2
    left_list = my_list[:middle]
    right_list = my_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge_list(left_list, right_list))


def merge_list(left_list, right_list):
    res = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list) == 0:
        res = res + right_list
    else:
        res = res + left_list
    return res


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))

t = timeit.timeit('merge_sort(unsorted_list)', 'from __main__ import merge_sort,unsorted_list', number=1000)
print(t)
