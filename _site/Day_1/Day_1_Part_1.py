import re

from day_1_puzzle_input import PUZZLE_INPUT

list_1 = []
list_2 = []

digit_regex = r"\d+\w"

number_input = re.findall(digit_regex, PUZZLE_INPUT)
for i in range(0,len(number_input),2):
    list_1.append(int(number_input[i]))
    list_2.append(int(number_input[i+1]))

list_1.sort()
list_2.sort()
sum = 0

for item_1, item_2 in zip(list_1,list_2):
    distance = abs(item_1-item_2)
    sum = sum + distance

print(sum)