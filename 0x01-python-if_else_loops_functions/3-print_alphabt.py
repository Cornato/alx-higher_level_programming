#!/usr/bin/python3
current_char = ord('a')

while current_char <= ord('z'):
    if chr(current_char) != 'q' and chr(current_char) != 'e':
        print('{}'.format(chr(current_char)), end='')
    current_char += 1
