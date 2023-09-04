#!/usr/bin/python3
"""Cimporting the sys module"""
import sys


def is_safe(bod, row, col, n):
    for i in range(row):
        if bod[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if bod[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if bod[i][j] == 1:
            return False
    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(bod, row):
        if row == n:
            sol.append([(i, row.index(1)) for i, row in enumerate(bod)])
            return
        for col in range(n):
            if is_safe(bod, row, col, n):
                bod[row][col] = 1
                backtrack(bod, row + 1)
                bod[row][col] = 0
    sol = []
    bod = [[0] * n for _ in range(n)]
    backtrack(bod, 0)
    for soln in sol:
        print(soln)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)
