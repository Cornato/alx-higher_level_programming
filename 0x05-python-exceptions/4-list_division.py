#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        Value = 0
        try:
            if type(my_list_1[i]) not in [int, float]:
                raise TypeError("wrong type")
            if type(my_list_2[i]) not in [int, float]:
                raise TypeError("wrong type")
            Value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(Value)
    return new_list
