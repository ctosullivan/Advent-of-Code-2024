import re
from collections import defaultdict
from pprint import pprint
from itertools import combinations

from Day_8_Puzzle_Input import PUZZLE_INPUT

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
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
        # Use combinations to get unique pairs
        for (r1, c1), (r2, c2) in combinations(antennas, 2):
            # Calculate distance vectors
            delta_r, delta_c = abs(r2 - r1), abs(c2 - c1)

            # Calculate antinodes
            match r1 > r2:
                case True:
                    match c1 > c2:
                        case True:
                            # r1 > r2, c1 > c2
                            antinode1 = (r1 + delta_r, c1 - delta_c)
                            antinode2 = (r2 - delta_r, c2 + delta_c)
                        case False:
                            # r1 > r2, c1 < c2
                            antinode1 = (r1 - delta_r, c1 + delta_c)
                            antinode2 = (r2 - delta_r, c2 - delta_c)
                case False:
                    match c1 > c2:
                        case True:
                            # r1 < r2, c1 > c2
                            antinode1 = (r1 - delta_r, c1 + delta_c)
                            antinode2 = (r2 + delta_r, c2 - delta_c)
                        case False:
                            # r1 < r2, c1 < c2
                            antinode1 = (r1 - delta_r, c1 - delta_c)
                            antinode2 = (r2 + delta_r, c2 + delta_c)

            # Add antinodes if within bounds
            for ar, ac in [antinode1, antinode2]:
                if 0 <= ar < rows and 0 <= ac < cols:
                    antinodes.add((ar, ac))

    # Return the count of unique antinode locations
    return len(antinodes)


print(find_antinodes(PUZZLE_INPUT))