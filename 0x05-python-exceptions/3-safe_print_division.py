#!/usr/bin/python3
def safe_print_division(a, b):
    Value = 0.0
    try:
        Value = a / b
    except (TypeError, ZeroDivisionError):
        Value = None
    finally:
        print("Inside result: {}".format(Value))
    return Value
