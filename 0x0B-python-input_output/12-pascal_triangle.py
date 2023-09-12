#!/usr/bin/python3
"""
Returns a list of lists of integers
reps the Pascal triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    res = []
    lis = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(lis[y] + lis[y - 1])
        lis = row
        res.append(row)
    return res
