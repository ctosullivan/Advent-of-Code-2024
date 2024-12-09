from Day_9_Puzzle_Input import PUZZLE_INPUT

test_input = "2333133121414131402"

def solution(input_string):
    disk_map_string = input_string

    def parse_input_string(input_string):
        parsed_string = []
        input_string = input_string.strip()
        # parses the input string and returns a list of strings
        for i in range(len(input_string)):
            parsed_string.append(input_string[i])
        return parsed_string
    
    def read_disk_map(parsed_input_list):
        # reads the file map and returns a string representing the unpacked file
        unpacked_file = []
        block_id = 0
        for i in range(0, len(parsed_input_list), 2):
            block_length = int(parsed_input_list[i])
            if i < len(parsed_input_list) - 1:
                block_padding = int(parsed_input_list[i+1])
            # End of disk map - no padding required
            else: block_padding = None
            unpacked_file.append(str(block_id) * block_length)
            if block_padding is not None:
                unpacked_file.append("." * block_padding)
            block_id += 1
        return "".join(unpacked_file)

    def recompress_file(unpacked_file):
        unpacked_file_list = [i for i in unpacked_file]
        eof_pointer = len(unpacked_file_list) - 1
        compressed_file = []
        i = 0
        while i <= eof_pointer:
            if unpacked_file_list[eof_pointer] == ".":
                unpacked_file_list.pop()
                eof_pointer -= 1
                continue
            elif unpacked_file_list[i] == ".":
                compressed_file.append(unpacked_file_list.pop())
                eof_pointer -= 1
                i += 1
            else:
                compressed_file.append(unpacked_file_list[i])
                i += 1
        return "".join(compressed_file)

    def get_file_checksum(compressed_file):
        check_sum = 0
        for i in range(len(compressed_file)):
            j = int(compressed_file[i])
            check_sum += i * j
        return check_sum

    parsed_input_list = parse_input_string(disk_map_string)
    unpacked_file = read_disk_map(parsed_input_list)
    compressed_file = recompress_file(unpacked_file)
    print(parsed_input_list)
    return get_file_checksum(compressed_file)

print(solution(PUZZLE_INPUT))