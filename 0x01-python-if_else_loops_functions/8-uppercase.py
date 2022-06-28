#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        if ord(str[a]) in range(97, 123):
            diff = 32
        else:
            diff = 0
    print("{:c}".format(str[a]- diff), end="")
