#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = new_element
    return new_list
