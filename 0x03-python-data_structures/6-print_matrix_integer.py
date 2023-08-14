#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        for i in range(len(row)):
            print("{:d}".format(row[i]),end="\n"if i == len(row) - 1 else '')
