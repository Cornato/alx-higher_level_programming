def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list) - 1, -1):
        print("{:d}".format(my_list[i]))
