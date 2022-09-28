#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for j in set(my_list):
        add += j
    return add
