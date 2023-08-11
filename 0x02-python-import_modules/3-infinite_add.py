#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = sys.argv[1:]
    total = sum(int(arg) for arg in argc)
    print(total)
