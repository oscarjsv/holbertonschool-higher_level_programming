#!/usr/bin/python3
def uppercase(str):
    list = ""
    for i in range(len(str)):
        if ord(str[i]) >= (97) and ord(str[i]) <= (122):
            list += chr(ord(str[i]) - 32)
        else:
            list += chr(ord(str[i]))
    print("{:}".format(list))
