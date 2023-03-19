#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or not my_list:
        return 0
    sum = 0
    size = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        size += tup[1]
    return sum / size
