import re
from collections import Counter

from day_1_puzzle_input import PUZZLE_INPUT

list_1 = []
list_2 = []
similarity_score = 0

digit_regex = r"\d+\w"

number_input = re.findall(digit_regex, PUZZLE_INPUT)
for i in range(0,len(number_input),2):
    list_1.append(int(number_input[i]))
    list_2.append(int(number_input[i+1]))

count_2 = Counter(list_2)

for i in list_1:
    if i in count_2:
        similarity_score = similarity_score + (i * (count_2[i]))

print(similarity_score)