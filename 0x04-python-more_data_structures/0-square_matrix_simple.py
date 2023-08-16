#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squares = [value ** 2 for value in row]
        new_matrix.append(squares)
    return new_matrix
