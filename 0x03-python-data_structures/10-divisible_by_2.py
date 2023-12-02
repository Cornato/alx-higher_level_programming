#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nList = []
    for x in sorted(my_list):
        nList.append(True if x % 2 == 0 else False)
    return nList
