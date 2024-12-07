from itertools import product

from Day_7_Puzzle_Input import PUZZLE_INPUT

test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def parse_input(input_data):
    # returns a list of equations in the format target, numbers
    equations = []
    for line in input_data.strip().split("\n"):
        target, nums = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, nums.strip().split()))
        equations.append((target, numbers))
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def find_total_calibration_result(input_data):
    equations = parse_input(input_data)
    total_result = 0

    for target, numbers in equations:
        num_operators = len(numbers) - 1
        all_operator_combinations = product(["+","*"], repeat=num_operators)
    
        valid = False
        for operators in all_operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break
        if valid:
            total_result += target

    return total_result

print(find_total_calibration_result(PUZZLE_INPUT))