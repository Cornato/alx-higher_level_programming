#!/usr/bin/python3
i = ord('z')

while i >= ord('a'):
    if i % 2 != 0:
        print('{}'.format(chr(i - 32)), end='')
    else:
        print('{}'.format(chr(i)), end='')
    i -= 1
