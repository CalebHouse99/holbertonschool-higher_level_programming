#!/usr/bin/python3

for i in range(97, 123):
    x = chr(i)
    if x == 'q' or x == 'e':
        continue
    print(x.format(x), end='')
