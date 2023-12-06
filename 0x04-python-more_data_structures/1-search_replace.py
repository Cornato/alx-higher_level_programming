#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nList = []
    for i in my_list:
        if i == search:
            nList.append(replace)
        else:
            nList.append(i)
    return nList
