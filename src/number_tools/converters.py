import sys

INTEGER_TO_ROMAN_SET = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)

ROMAN_TO_INTEGER_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def integer_to_roman(integer):
    roman_numeral = ""
    i = 0
    while integer > 0:
        while INTEGER_TO_ROMAN_SET[i][1] > integer:
            i += 1
        roman_numeral += INTEGER_TO_ROMAN_SET[i][0]
        integer -= INTEGER_TO_ROMAN_SET[i][1]
    return roman_numeral


def roman_to_integer(roman_numeral):
    total = 0
    last_value = sys.maxsize
    for char in list(roman_numeral):
        value = ROMAN_TO_INTEGER_MAP[char.upper()]
        if value > last_value:
            total += value - 2 * last_value
        else:
            total += value
        last_value = value
    return total
