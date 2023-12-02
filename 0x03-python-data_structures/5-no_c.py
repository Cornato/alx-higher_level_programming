#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for name in range(len(my_string)):
    	if my_string[name] != 'c' or my_string[name] != 'C':
         result += my_string[name]
        else:
         result += ''
         
    return result
