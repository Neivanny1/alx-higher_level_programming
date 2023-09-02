#!/usr/bin/pyton3
def safe_print_list(my_list=[], x=0):
    num = 0
    for x in range (0, x):
        try:
            print(my_list[x], end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)
