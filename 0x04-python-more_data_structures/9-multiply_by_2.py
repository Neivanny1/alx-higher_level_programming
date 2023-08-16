#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, item in a_dictionary.items():
        new_dict[key] = item * 2
    return new_dict
