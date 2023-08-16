#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqs = set()
    total = 0
    for num in my_list:
        if num not in uniqs:
            total += num
            uniqs.add(num)
    return total
