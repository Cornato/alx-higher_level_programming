#!/usr/bin/python3
def uppercase(s):
    result = ""
    index = 0

    while index < len(s):
        char = s[index]

        if 'a' <= char <= 'z':
            result += '{}'.format(chr(ord(char) - 32))
        else:
            result += char

        index += 1

    print(result)
