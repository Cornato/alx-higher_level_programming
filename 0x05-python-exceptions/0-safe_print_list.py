#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            value += 1
        print()
        return value
    except IndexError:
        print()
        return value
