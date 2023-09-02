#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = sum(1 for x in my_list)
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            i = i + 1
            count = count - 1
        finally:
            count = count + 1
    print()
    return count
