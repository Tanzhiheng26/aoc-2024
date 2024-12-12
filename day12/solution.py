DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def inbounds(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def get_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c, value, region):
        if not inbounds(r, c, grid) or grid[r][c] != value or (r, c) in visited:
            return
        
        visited.add((r, c))
        region.append((r, c))
        
        for dr, dc in DIRECTIONS:
            new_r = r + dr
            new_c = c + dc
            dfs(new_r, new_c, value, region)
    
    regions = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region = []
                dfs(r, c, grid[r][c], region)
                regions.append(region)

    return regions

def calc_perimeter(region, grid):
    perimeter = 0
    
    for r, c in region:
        for dr, dc in DIRECTIONS:
            new_r = r + dr
            new_c = c + dc
            if not inbounds(new_r, new_c, grid) or grid[new_r][new_c] != grid[r][c]:
                perimeter += 1

    return perimeter


def part1(file):
    grid = read_input(file) 
    regions = get_regions(grid)
    price = 0

    for region in regions:
        area = len(region)
        perimeter = calc_perimeter(region, grid)
        price += area * perimeter

    return price

def check_corners(r, c, neighbors, grid):
    n = len(neighbors)
    if n == 0:
        return 4
    elif n == 1:
        return 2
    elif n == 2:
        r1, c1 = neighbors[0]
        r2, c2 = neighbors[1]
        if r1 == r2 or c1 == c2:
            """
            XXX 
            or 
            X
            X
            X
            """
            return 0
        else:
            """
            X?
            XX
            """
            # ? represents (r3, c3) 
            r3 = r1 if r1 != r else r2
            c3 = c1 if c1 != c else c2
            return 1 + (grid[r3][c3] != grid[r][c])
    elif n == 3:
        """
        ?X?
        XXX
        """
        # ? represents (r4, c4) and (r5, c5)
        r1, c1 = neighbors[0]
        r2, c2 = neighbors[1]
        r3, c3 = neighbors[2]
        diff_r = [i for i in (r1, r2, r3) if i != r]
        diff_c = [i for i in (c1, c2, c3) if i != c]
        if len(diff_r) == 1 and len(diff_c) == 2:
            r4 = r5 = diff_r[0]
            c4, c5 = diff_c
            return (grid[r4][c4] != grid[r][c]) + (grid[r5][c5] != grid[r][c])
        elif len(diff_r) == 2 and len(diff_c) == 1:
            r4, r5 = diff_r
            c4 = c5 = diff_c[0]
            return (grid[r4][c4] != grid[r][c]) + (grid[r5][c5] != grid[r][c])
    else: # n == 4
        """
        ?X?
        XXX
        ?X?
        """
        # ? represents (r5, c5), (r6, c6), (r7, c7), (r8, c8)
        r1, c1 = neighbors[0]
        r2, c2 = neighbors[1]
        r3, c3 = neighbors[2]
        r4, c4 = neighbors[3]
        diff_r = [i for i in (r1, r2, r3, r4) if i != r]
        diff_c = [i for i in (c1, c2, c3, c4) if i != c]
        r5 = r6 = diff_r[0]
        r7 = r8 = diff_r[1]
        c5 = c7 = diff_c[0]
        c6 = c8 = diff_c[1]
        return ((grid[r5][c5] != grid[r][c]) 
                + (grid[r6][c6] != grid[r][c])
                + (grid[r7][c7] != grid[r][c]) 
                + (grid[r8][c8] != grid[r][c]))

# Hint from https://www.reddit.com/r/adventofcode/comments/1hcf16m/2024_day_12_everyone_must_be_hating_today_so_here/
# Number of sides = number of corners
def num_corners(region, grid):
    corners = 0
    
    for r, c in region:
        neighbors = [] # neighbors with same value
        for dr, dc in DIRECTIONS:
            new_r = r + dr
            new_c = c + dc
            if inbounds(new_r, new_c, grid) and grid[new_r][new_c] == grid[r][c]:
                neighbors.append((new_r, new_c))
        corners += check_corners(r, c, neighbors, grid)

    return corners

def part2(file):
    grid = read_input(file) 
    regions = get_regions(grid)
    price = 0

    for region in regions:
        area = len(region)
        sides = num_corners(region, grid)
        price += area * sides

    return price


print(part1("input.txt"))
print(part2("input.txt"))
