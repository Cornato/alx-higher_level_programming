def print_matrix_integer(matrix=[]):
    for row in matrix:
        for i in row:
            if i == len(row):
                print("{:d}".format(i), end="")
            else:
                print("{:d} ".format(i), end="")
        print()
