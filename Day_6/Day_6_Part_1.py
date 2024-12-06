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

from Day_6_Puzzle_Input import PUZZLE_INPUT

# Convert input to 2D array
input_array = [list(row) for row in PUZZLE_INPUT.splitlines()]

def move_in_array(puzzle_array):
    while True:
        def turn_90_degrees(direction):
            match direction:
                case -1, 0:
                    new_direction = 0, 1
                case 0, 1:
                    new_direction = 1, 0
                case 1, 0:
                    new_direction = 0, -1
                case 0, -1:
                    new_direction = -1, 0
            return new_direction

        # get current position & direction
        for i in range(len(puzzle_array)):
            for j in range(len(puzzle_array[0])):
                if puzzle_array[i][j] == "^":
                    position = i, j
                    direction = -1, 0
                elif puzzle_array[i][j] == ">":
                    position = i, j
                    direction = 0, 1
                elif puzzle_array[i][j] == "V":
                    position = i, j
                    direction = 1, 0
                elif puzzle_array[i][j] == "<":
                    position = i, j
                    direction = 0, -1
        puzzle_array[position[0]][position[1]] = "X"
        
        # check validity of new position
        new_position = (position[0] + direction[0], position[1] + direction[1])
        try:
            puzzle_array[new_position[0]][new_position[1]] is not None
        except IndexError:
            # new position is out of bounds - end loop
            result = 0
            for i in range(len(puzzle_array)):
                for j in range(len(puzzle_array[0])):
                    if puzzle_array[i][j] == "X":
                        result += 1
            return result

        # if there is an X in the new position, turn 90 degrees
        if puzzle_array[new_position[0]][new_position[1]] == "#":
            direction = turn_90_degrees(direction)
            new_position = (position[0] + direction[0], position[1] + direction[1])
        position = new_position

result = move_in_array(input_array)

print(result)