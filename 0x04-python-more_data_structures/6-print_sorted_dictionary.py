#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _keys = sorted(a_dictionary.keys())

    for key in _keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
