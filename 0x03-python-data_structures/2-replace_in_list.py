#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new = []
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        new = my_list
        return new
