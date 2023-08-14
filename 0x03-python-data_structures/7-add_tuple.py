#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 2 and len1 != 0:
        list_a = list(tuple_a)
        list_a.append(0)
        tuple_a = tuple(list_a)
    elif len1 == 0:
        list_a = list(tuple_a)
        list_a.append(0)
        list_a.append(0)
        tuple_a = tuple(list_a)
    elif len1 > 2:
        tuple_a = tuple_a[:2]

    if len2 < 2 and len2 != 0:
        list_a = list(tuple_b)
        list_a.append(0)
        tuple_b = tuple(list_a)
    elif len2 == 0:
        list_a = list(tuple_b)
        list_a.append(0)
        list_a.append(0)
        tuple_b = tuple(list_a)
    elif len2 > 2:
        tuple_b = tuple_b[:2]
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
