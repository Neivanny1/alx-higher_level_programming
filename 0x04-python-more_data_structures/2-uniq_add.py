#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqs = set(my_list)
    total = 0
    for num in uniqs:
        total += num
    return total
