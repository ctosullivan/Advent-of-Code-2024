from Day_6_Puzzle_Input import PUZZLE_INPUT

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

input_array = [list(row) for row in PUZZLE_INPUT.splitlines()]

def count_obstruction_positions(grid):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    # Parse the grid to find the guard's starting position and direction
    rows, cols = len(grid), len(grid[0])
    start_pos, start_dir = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                start_pos = (r, c)
                start_dir = direction_map[grid[r][c]]
                break
        if start_pos:
            break

    # Helper to determine the next state based on current position and direction
    def next_state(r, c, direction, obstruction=None):
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        # Check out-of-bounds
        if not (0 <= nr < rows and 0 <= nc < cols):
            return None  # Path ends

        # Check for obstacles or obstruction
        if grid[nr][nc] == '#' or (nr, nc) == obstruction:
            # Turn right
            return (r, c, (direction + 1) % 4)

        # Move forward
        return (nr, nc, direction)

    # Simulate the guard's movement to detect a loop or return the full path
    def get_guard_path(r, c, direction, obstruction=None):
        path = []
        visited = set()

        while True:
            state = (r, c, direction)
            if state in visited:
                return True  # Loop detected
            visited.add(state)
            path.append((r, c, direction))  # Record position
            next_s = next_state(r, c, direction, obstruction)
            if next_s is None:  # Path ends
                break
            r, c, direction = next_s
        return path

    # Simulate the guard's movement to detect a loop only
    def causes_loop(r, c, direction, obstruction):
        path_or_loop = get_guard_path(r, c, direction, obstruction)
        return path_or_loop is True  # True if a loop is detected

    # Get all valid positions on the grid
    valid_positions = [
        (r, c) for r in range(rows) for c in range(cols)
        if grid[r][c] == '.' and (r, c) != start_pos
    ]

    # Test each position for obstruction placement
    obstruction_count = 0
    for r, c in valid_positions:
        if causes_loop(start_pos[0], start_pos[1], start_dir, obstruction=(r, c)):
            obstruction_count += 1

    return obstruction_count

# Example usage
print(count_obstruction_positions(input_array))
