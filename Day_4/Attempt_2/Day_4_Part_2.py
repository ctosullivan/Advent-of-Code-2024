# Example Test Input
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
from Day_4_puzzle_input import PUZZLE_INPUT

# Convert input to 2D array
input_array = [list(row) for row in PUZZLE_INPUT.splitlines()]
xmas_count = 0

# Helper function to check for "MAS" in an X pattern
def check_pattern(array, row, col):
    rows = len(array)
    cols = len(array[0])

    # Ensure all diagonal positions are within bounds
    if not (0 <= row - 1 < rows and 0 <= col - 1 < cols):
        return False
    if not (0 <= row + 1 < rows and 0 <= col + 1 < cols):
        return False
    if not (0 <= row + 1 < rows and 0 <= col - 1 < cols):
        return False
    if not (0 <= row - 1 < rows and 0 <= col + 1 < cols):
        return False

    # Check the "MAS" pattern in both diagonal directions
    top_left_to_bottom_right = (
        (array[row - 1][col - 1] == "M" and array[row][col] == "A" and array[row + 1][col + 1] == "S") or (array[row + 1][col + 1] == "M" and array[row][col] == "A" and array[row - 1][col - 1] == "S") 
    )
    top_right_to_bottom_left = (
        (array[row - 1][col + 1] == "M" and array[row][col] == "A" and array[row + 1][col - 1] == "S") or (array[row + 1][col - 1] == "M" and array[row][col] == "A" and array[row - 1][col + 1] == "S")
    )

    # Return true if either diagonal forms a valid "MAS" pattern
    return top_left_to_bottom_right and top_right_to_bottom_left

# Iterate through the 2D array
for row in range(len(input_array)):
    for col in range(len(input_array[0])):
        if input_array[row][col] == "A":  # Center of the "MAS" pattern
            if check_pattern(input_array, row, col):
                xmas_count += 1

print(f"Number of X-MAS patterns found: {xmas_count}")
