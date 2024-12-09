test_input = "12345"

def solution(input_string):

    def parse_input_string(input_string):
        parsed_string = []
        # parses the input string and returns a list of strings
        for i in range(len(input_string)):
            parsed_string.append(input_string[i])

print(solution(test_input))