#!/usr/bin/python3
for asci in range(122, 96, -1):
    if asci % 2 != 0:
        asci -= 32
    print("{}".format(chr(asci)), end="")
