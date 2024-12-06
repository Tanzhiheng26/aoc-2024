DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

TURN_RIGHT = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def get_starting_position(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in DIRECTIONS:
                return (r, c), DIRECTIONS[grid[r][c]]

def in_bounds(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def visited_positions(file):
    grid = read_input(file)
    position, direction = get_starting_position(grid)
    r, c = position
    dr, dc = direction
    visited = set()

    while in_bounds(grid, r, c):
        visited.add((r, c))
        wall_ahead = in_bounds(grid, r + dr, c + dc) and grid[r + dr][c + dc] == '#' 
        if wall_ahead:
            dr, dc = TURN_RIGHT[dr, dc]
            # don't increment r and c first since it is possible 
            # to turn right and be faced with another wall.
        else:
            r += dr
            c += dc
    
    return visited

def has_loop(start_pos, start_dir, grid):
    r, c = start_pos
    dr, dc = start_dir
    visited = set()

    while in_bounds(grid, r, c):
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        wall_ahead = in_bounds(grid, r + dr, c + dc) and grid[r + dr][c + dc] == '#'
        if wall_ahead:
            dr, dc = TURN_RIGHT[dr, dc]
        else:
            r += dr
            c += dc
    
    return False
    
def part2(file):
    grid = read_input(file)
    start_pos, start_dir = get_starting_position(grid)
    visited = visited_positions(file)

    result = 0
    for r, c in visited:
        # new obstruction can't be placed at the guard's starting position
        if grid[r][c] != '.':
            continue
        grid[r][c] = '#'
        if has_loop(start_pos, start_dir, grid):
            result += 1
        grid[r][c] = '.'
    
    return result

print("Part 1:", len(visited_positions("input.txt")))
print("Part 2:", part2("input.txt"))