#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    value_index = []
    start = -1
    while True:
        try:
            start = list(a_dictionary.values()).index(value, start + 1)
            value_index.append(start)
        except(ValueError):
            break
    for index, key in enumerate(list(a_dictionary)):
        if index in value_index:
            del a_dictionary[key]
    return a_dictionary
