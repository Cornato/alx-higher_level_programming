#!/usr/bin/python3
current_char = ord('a')

while current_char <= ord('z'):
    print('{}'.format(chr(current_char)), end='')
    current_char += 1
