from Day_5_Puzzle_Input import input_rules, input_updates

test_rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

test_updates="""75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

updates_array = [list(row.split(",")) for row in input_updates.splitlines()]
rules_list_array = [list(row.split("|")) for row in input_rules.splitlines()]
# convert updates array to int
updates_array = [[int(value) for value in row] for row in updates_array]


rules_dict = {}
for rule in rules_list_array:
    if int(rule[0]) not in rules_dict.keys():
        rules_dict[int(rule[0])] = []
        rules_dict[int(rule[0])].append(int(rule[1]))
    elif int(rule[0]) in rules_dict.keys():
        rules_dict[int(rule[0])].append(int(rule[1]))

def check_update(update_array, rules_dict):
    # Function to check if an update is valid
    # Returns true if valid, false if not
    for page in update_array:
        if page in rules_dict.keys():
            order_array = rules_dict[page]
            for rule in order_array:
                if rule in update_array:
                    if update_array.index(page) > update_array.index(rule):
                        # page breaks one of the rules
                        return False
    return True

result = 0
for array in updates_array:
    if check_update(array, rules_dict):
        result += array[len(array) // 2]

print(result)

