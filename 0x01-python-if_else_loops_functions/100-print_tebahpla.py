#!/usr/bin/python3
small = False
for letter in range(ord('z'), ord('a')-1, -1):
    if small:
        letter -= 32
    small = not small
    print("{}".format(chr(letter)), end="")
