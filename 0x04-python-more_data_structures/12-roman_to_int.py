#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    num = 0
    previous_roman = 'I'
    for roman_num in roman_string[::-1]:
        if roman_values[previous_roman] > roman_values[roman_num]:
            num -= roman_values[roman_num]
        num += roman_values[roman_num]
        previous_num = roman_num
    return num
