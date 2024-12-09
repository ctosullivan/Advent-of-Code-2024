import re

from Day_2_puzzle_input import PUZZLE_INPUT

test_levels = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

safe = 0
levels_list = []

level_regex = re.compile(r"^[\d ]+$", re.M)
level_input = re.findall(level_regex, PUZZLE_INPUT)
for level in level_input:
    levels_list.append(level.split())

def level_validation(report):
    """ Function to check if a report is safe or not.
    Returns true if all conditions are met:
        - All levels in the report are either increasing or decreasing
        - Any two adjacent levels differ by at least one and at most three
    """
    def check_adjacency(i,j):
        # Validates two adjacent levels
        # Returns true if any two adjacent levels differ by at least one and at most three
        if abs(i - j) >= 1 and abs(i - j) <= 3:
            return True
        else:
            return False

    if report[1] > report[0] and check_adjacency(report[1], report[0]):
        # Increasing - check if all levels are increasing
        for i in range(2,len(report)):
            if report[i] > report[i-1] and check_adjacency(report[i], report[i-1]):
                continue
            else:
                return False
        # All conditions in report met - report is safe
        return True
    elif report[1] < report[0] and check_adjacency(report[1], report[0]):
        # Decreasing - check if all reports are decreasing
        for i in range(2,len(report)):
            if report[i] < report[i-1] and check_adjacency(report[i], report[i-1]):
                continue
            else:
                return False
        # All conditions in report met - report is safe
        return True

for report in levels_list:
    for i in range(len(report)):
        report[i] = int(report[i])
    if level_validation(report):
        safe += 1
    else:
        # Loop through report to check if we can remove a level to make it safe
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            if level_validation(report_copy):
                safe += 1
                break

print(safe)