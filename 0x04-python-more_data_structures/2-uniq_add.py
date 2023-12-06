#!/usr/bin/python3
def uniq_add(my_list=[]):
    integers = set()
    sum = 0

    for element in my_list:
        if element not in integers:
            integers.add(element)
            sum += element

    return sum
