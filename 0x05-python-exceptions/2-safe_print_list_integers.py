#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            count_printed += 1
    print()
    return count_printed
