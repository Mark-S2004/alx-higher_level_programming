#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) != 2:
        print("s", end="")
    if len(argv) == 1:
        print(".")
    else:
        print(":")
    for arg_index in range(1, len(argv)):
        print("{}: {}".format(arg_index, argv[arg_index]))
