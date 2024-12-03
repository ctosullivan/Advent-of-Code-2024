import re

from Day_3_puzzle_input import PUZZLE_INPUT

# trim puzzle input first

trim_regex = re.compile(r"(?=don't\(\)).*?(do\(\))|(?=don't\(\)).*", re.I|re.M|re.S)

PUZZLE_INPUT = re.sub(trim_regex, "", PUZZLE_INPUT)

multiplier_regex = re.compile(r'mul\((?P<first_digits>\d{1,3}),(?P<second_digits>\d{1,3})\)',re.M|re.I)

multipliers = multiplier_regex.findall(PUZZLE_INPUT)
result = 0

for multiplier in multipliers:
    first_digits, second_digits = multiplier
    first_digits = int(first_digits)
    second_digits = int(second_digits)
    result = result + (first_digits * second_digits)

print(result)