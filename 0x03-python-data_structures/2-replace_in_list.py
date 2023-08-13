#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = new_element
        new_list = my_list
        return my_list
