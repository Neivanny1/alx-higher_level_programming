#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]
    print("{} argument{}:".format(argc, "s" if argc != 1 else ""), end="")
    if argc == 0:
        print(".")
    else:
        print("")
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
