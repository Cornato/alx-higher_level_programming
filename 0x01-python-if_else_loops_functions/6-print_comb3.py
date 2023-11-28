#!/usr/bin/python3
i = 0

while i < 10:
    j = i + 1
    while j < 10:
        if i != j:
            separator = ", " if (i < 8 or j < 9) else "\n"
            print("{:d}{:d}".format(i, j), end=separator)
        j += 1
    i += 1
