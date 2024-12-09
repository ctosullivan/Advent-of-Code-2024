import re
from collections import defaultdict
from pprint import pprint
from itertools import permutations

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

"""
Calculate location of an antinode:
1. loop through the array and add antennae to dict
3. Calculate distance between each pair of antennae (x & y)
4. Add antinodes to array based on distance if within bounds
5. Count antinodes
    
"""

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

    for antenna in antennae_dict:
        if len(antennae_dict[antenna]) == 1:
            # Only one antenna, therefore no antinodes - remove from dict
            antennae_dict.pop(antenna)
            continue
        else:
            for permutation in permutations(antennae_dict[antenna]):
                # check first two values in each permutation only
                rd = abs(permutation[0][0]-permutation[1][0])
                cd = abs(permutation[0][1]-permutation[1][1])
                # get antinodes
                if permutation[0][0] > permutation[1][0]:
                    ar1 = permutation[0][0] + rd
                    ar2 = permutation[1][0] - rd
                else:
                    ar1 = permutation[0][0] - rd
                    ar2 = permutation[1][0] + rd

                if permutation[0][1] > permutation[1][1]:
                    ac1 = permutation[0][1] + cd
                    ac2 = permutation[1][1] - cd
                else:
                    ac1 = permutation[0][1] - cd
                    ac2 = permutation[1][0] + cd
                if (0 <= ac1 and ac1 <= cols) and (0 <= ar1 and ar1 <= rows):
                    antinodes.add((ac1, ar1))
                if (0 <= ac2 and ac2 <= cols) and (0 <= ar2 and ar2 <= rows):
                    antinodes.add((ac2, ar2))
    print(antinodes, len(antinodes))

find_antinodes(test_input)