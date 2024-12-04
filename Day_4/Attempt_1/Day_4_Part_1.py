import re

from Day_4_puzzle_input import PUZZLE_INPUT

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

# Convert input to 2d array
input_array = PUZZLE_INPUT.splitlines()
for i in range(len(input_array)):
    input_array[i] = input_array[i].split()
    for letter in input_array[i][0]:
        input_array[i].append(letter)
    input_array[i] = input_array[i][1:]

xmas_regex = re.compile(r"(?=XMAS)|(?<=SAMX)",flags=re.IGNORECASE|re.MULTILINE|re.DOTALL)
xmas_count = 0
horizontal_slices = []
vertical_slices = []
diagonal_slices = []

# Make array of horizontal slices
for row in range(len(input_array)):
    horizontal_slices.append("".join(input_array[row]))

# Make array of vertical slices
for col in range(len(input_array[0])):
    slice = []
    for row in range(len(input_array)):
        slice.append(input_array[row][col])
    vertical_slices.append("".join(slice))

# Get diagonal slices
cols = len(input_array[0])
rows = len(input_array)
diagonal_slices = []

# Get right diagonals
for col in range(cols):
    r, c = 0, col 
    diagonal = []
    while r < rows and c < cols:
        diagonal.append(input_array[r][c])
        r += 1  # Move down
        c += 1  # Move right
    diagonal_slices.append("".join(diagonal))

for row in range(1, rows):
    r, c = row, 0 
    diagonal = []
    while r < rows and c < cols:
        diagonal.append(input_array[r][c])
        r += 1  # Move down
        c += 1  # Move right
    diagonal_slices.append("".join(diagonal))

# Get left diagonals
for col in range(cols - 1, -1, -1):
    r, c = 0, col
    diagonal = []
    while r < rows and c >= 0:
        diagonal.append(input_array[r][c])
        r += 1  # Move down
        c -= 1  # Move left
    diagonal_slices.append("".join(diagonal))

for row in range(1, rows):
    r, c = row, cols - 1
    diagonal = []
    while r < rows and c >= 0:
        diagonal.append(input_array[r][c])
        r += 1  # Move down
        c -= 1  # Move left
    diagonal_slices.append("".join(diagonal))

for slice in horizontal_slices:
    matches = re.findall(xmas_regex, slice)
    xmas_count += len(matches)
horizontal = xmas_count

for slice in vertical_slices:
    matches = re.findall(xmas_regex, slice)
    xmas_count += len(matches)
vertical = xmas_count - horizontal

for slice in diagonal_slices:
    matches = re.findall(xmas_regex, slice)
    xmas_count += len(matches)

diagonal = xmas_count - vertical - horizontal
print(f"horizontal: {horizontal}")
print(f"vertical: {vertical}")
print(f"diagonal: {diagonal}")
print(f"total: {xmas_count}")

print(f"puzzle width: {len(input_array[0])}")
print(f"puzzle height: {len(input_array)}")