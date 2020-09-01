#!/usr/bin/python3
for number in range(00, 99):
    print("{:02d}".format(number), end=(', '))
    if number == 98:
        print(99)
    