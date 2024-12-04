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

# Convert input to 2D array
input_array = [list(row) for row in PUZZLE_INPUT.splitlines()]
xmas_count = 0

# Helper function to check bounds and match the pattern "MAS"
def check_pattern(array, start_row, start_col, d_row, d_col):
    rows = len(array)
    cols = len(array[0])

    # Check bounds for the full "MAS" pattern
    for step in range(1, 4):  # Check next 3 characters
        new_row = start_row + step * d_row
        new_col = start_col + step * d_col
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            return False  # Out of bounds
    # If in bounds, check the characters
    return (
        array[start_row + d_row][start_col + d_col] == "M" and
        array[start_row + 2 * d_row][start_col + 2 * d_col] == "A" and
        array[start_row + 3 * d_row][start_col + 3 * d_col] == "S"
    )

# Directions: (d_row, d_col) pairs for the 8 possible "XMAS" directions
directions = [
    (-1, 0),  # 12:00 - Up
    (-1, -1), # 10:30 - Up-left diagonal
    (0, -1),  # 09:00 - Left
    (1, -1),  # 07:30 - Down-left diagonal
    (1, 0),   # 06:00 - Down
    (1, 1),   # 05:30 - Down-right diagonal
    (0, 1),   # 03:00 - Right
    (-1, 1)   # 01:30 - Up-right diagonal
]

# Iterate through the 2D array
for row in range(len(input_array)):
    for col in range(len(input_array[0])):
        if input_array[row][col] == "X":  # Start of "XMAS"
            for d_row, d_col in directions:
                if check_pattern(input_array, row, col, d_row, d_col):
                    xmas_count += 1

print(xmas_count)