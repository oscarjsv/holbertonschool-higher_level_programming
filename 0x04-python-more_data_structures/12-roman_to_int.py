#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if type(roman_string) == str:
        roman_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman_string = list(roman_string)

        res = [roman_integer.get(item, item) for item in roman_string]
        for i in range(0, len(res) - 1):
            if res[i] < res[i+1]:
                value -= res[i]
            else:
                value += res[i]
        value += res[-1]
        return value
    else:
        return 0
