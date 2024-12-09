import re
from collections import defaultdict
from pprint import pprint
from itertools import combinations
import math

from Day_8_Puzzle_Input import PUZZLE_INPUT

test_input = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
"""

def parse_input(input_string):
    # Returns a 2d array of strings
    input_array = []
    for line in input_string.splitlines():
        input_array.append([i for i in line])
    return(input_array)

def find_antinodes(input_string):
    input_array = parse_input(input_string)
    antinodes = set()

    antennae_dict = defaultdict(list)
    rows, cols = len(input_array), len(input_array[0])
    for r in range(rows):
        for c in range(cols):
            if re.match(r"[a-zA-Z0-9]", input_array[r][c]):
                antenna = input_array[r][c]
                antennae_dict[input_array[r][c]].append((r, c))

    # Process each frequency group
    for frequency, antennas in antennae_dict.items():
        for (x1, y1), (x2, y2) in combinations(antennas, 2):
            dx, dy = x2 - x1, y2 - y1
            gcd = abs(math.gcd(dx, dy))
            step_x, step_y = dx // gcd, dy // gcd

            # Extend in both directions
            for direction in (-1, 1):  # Backward (-1) and forward (1) extensions
                px, py = x1, y1
                while 0 <= px < rows and 0 <= py < cols:
                    antinodes.add((px, py))
                    px += direction * step_x
                    py += direction * step_y

    return len(antinodes)

print(find_antinodes(PUZZLE_INPUT))