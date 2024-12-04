def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
        return grid

# This word search allows words to be horizontal, vertical, diagonal, 
# written backwards, or even overlapping other words.
def find_xmas1(grid, r, c):
    # grid[r][c] == 'X'
    rows, cols = len(grid), len(grid[0])

    # XMAS
    east = (c + 3) < cols and grid[r][c + 1] == 'M' and grid[r][c + 2] == 'A' and grid[r][c + 3] == 'S'
    
    # SAMX
    west = (c - 3) >= 0 and grid[r][c - 3] == 'S' and grid[r][c - 2] == 'A' and grid[r][c - 1] == 'M'
    
    # X
    # M
    # A
    # S
    south = (r + 3) < rows and grid[r + 1][c] == 'M' and grid[r + 2][c] == 'A' and grid[r + 3][c] == 'S'
    
    # S
    # A
    # M
    # X
    north = (r - 3) >= 0 and grid[r - 3][c] == 'S' and grid[r - 2][c] == 'A' and grid[r - 1][c] == 'M'
    
    # X
    #  M
    #   A
    #    S
    southeast = (c + 3) < cols and (r + 3) < rows and grid[r + 1][c + 1] == 'M' and grid[r + 2][c + 2] == 'A' and grid[r + 3][c + 3] == 'S'
    
    # S
    #  A
    #   M
    #    X
    northwest = (c - 3) >= 0 and (r - 3) >= 0 and grid[r - 3][c - 3] == 'S' and grid[r - 2][c - 2] == 'A' and grid[r - 1][c - 1] == 'M'
    
    #    S
    #   A
    #  M
    # X
    northeast = (c + 3) < cols and (r - 3) >= 0 and grid[r - 1][c + 1] == 'M' and grid[r - 2][c + 2] == 'A' and grid[r - 3][c + 3] == 'S'
    
    #    X
    #   M
    #  A
    # S
    southwest = (c - 3) >= 0 and (r + 3) < rows and grid[r + 3][c - 3] == 'S' and grid[r + 2][c - 2] == 'A' and grid[r + 1][c - 1] == 'M'

    xmas_count = sum([east, west, south, north, southeast, northwest, northeast, southwest])
    return xmas_count

def part1(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                result += find_xmas1(grid, r, c)
    
    return result

def find_xmas2(grid, r, c):
    # grid[r][c] == 'A'
    rows, cols = len(grid), len(grid[0])
    if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
        return 0

    top_left = grid[r - 1][c - 1]
    top_right = grid[r - 1][c + 1]
    bottom_left= grid[r + 1][c - 1]
    bottom_right = grid[r + 1][c + 1]

    # M M
    #  A
    # S S
    mm = top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S'

    # S S
    #  A
    # M M
    ss = top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M'

    # M S
    #  A
    # M S
    ms = top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S'

    # S M
    #  A
    # S M
    sm = top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M'

    xmas_count = sum([mm, ss, ms, sm])
    return xmas_count

def part2(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                result += find_xmas2(grid, r, c)
    
    return result

print(part1("input.txt"))
print(part2("input.txt"))