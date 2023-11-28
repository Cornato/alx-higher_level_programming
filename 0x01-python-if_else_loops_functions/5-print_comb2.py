#!/usr/bin/python3
current_value = 0

while current_value < 100:
    if current_value == 99:
        print("{}".format(current_value))
    else:
        print("{:02}".format(current_value), end=", ")
    current_value += 1
