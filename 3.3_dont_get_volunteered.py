grid = [
[6,5,4,5,4,5,4,5,4,5,4,5,4,5,6,],
[5,4,5,4,3,4,3,4,3,4,3,4,5,4,5,],
[4,5,4,3,4,3,4,3,4,3,4,3,4,5,4,],
[5,4,3,4,3,2,3,2,3,2,3,4,3,4,5,],
[4,3,4,3,2,3,2,3,2,3,2,3,4,3,4,],
[5,4,3,2,3,4,1,2,1,4,3,2,3,4,5,],
[4,3,4,3,2,1,2,3,2,1,2,3,4,3,4,],
[5,4,3,2,3,2,3,0,3,2,3,2,3,4,5,],
[4,3,4,3,2,1,2,3,2,1,2,3,4,3,4,],
[5,4,3,2,3,4,1,2,1,4,3,2,3,4,5,],
[4,3,4,3,2,3,2,3,2,3,2,3,4,3,4,],
[5,4,3,4,3,2,3,2,3,2,3,4,3,4,5,],
[4,5,4,3,4,3,4,3,4,3,4,3,4,5,4,],
[5,4,5,4,3,4,3,4,3,4,3,4,5,4,5,],
[6,5,4,5,4,5,4,5,4,5,4,5,4,5,6,],
]

def get_directions(start, end, grid_size=8):
    """
    Returns the directions from start to end in the grid.
    """
    # Calculate row and column for start and end
    start_row, start_col = divmod(start, grid_size)
    end_row, end_col = divmod(end, grid_size)

    # Calculate the number of steps in each direction
    steps_right = end_col - start_col
    steps_down = end_row - start_row

    # Generate the directions based on the steps
    directions = (
        "R" * max(steps_right, 0)
        + "L" * max(-steps_right, 0)
        + "D" * max(steps_down, 0)
        + "U" * max(-steps_down, 0)
    )

    return directions

def is_valid_move(x, y, grid):
    """
    Returns True if the move is valid, False otherwise.
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def move(x, y, direction):
    """
    Returns the new position after moving in the given direction.
    """
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy
    return new_x, new_y

def navigator(path, grid):
    """
    Returns the value of the destination cell after following the given path.
    """
    current_x, current_y = 7, 7  # Starting position

    for move_direction in path:
        current_x, current_y = move(current_x, current_y, move_direction)
        if not is_valid_move(current_x, current_y, grid):
            return None  # Invalid move, return None

    return grid[current_x][current_y]

def solution(src, dest):
    # There are few exceptions where grid is changed depending on the knight's position

    # The knight being in the corners
    if src in [0, 7, 56, 63]:
        grid[6][6] = 4
        grid[6][8] = 4
        grid[8][6] = 4
        grid[8][8] = 4

    # The knight being in one diagonal away from the corners
    elif src == 9:
        grid[6][6] = 4

    elif src == 14:
        grid[6][8] = 4

    elif src == 49:
        grid[8][6] = 4

    elif src == 54:
        grid[8][8] = 4

    else:
        pass

    # Finding directions from src to dest
    directions = get_directions(src, dest)

    min_moves = navigator(directions, grid)

    return min_moves