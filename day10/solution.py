DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(map(int, line.strip())))
    return grid

def inbounds(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def part1(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c, prev_value, visited_nines):
        if not inbounds(r, c, grid) or grid[r][c] != prev_value + 1:
            return
        if grid[r][c] == 9:
            visited_nines.add((r, c))
            return
            
        for dr, dc in DIRECTIONS:
            dfs(r + dr, c + dc, grid[r][c], visited_nines)

    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                visited_nines = set()
                dfs(r, c, -1, visited_nines)
                total_score += len(visited_nines)
    
    return total_score

def part2(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c, prev_value):
        if not inbounds(r, c, grid) or grid[r][c] != prev_value + 1:
            return 0
        if grid[r][c] == 9:
            return 1
        
        rating = 0
        for dr, dc in DIRECTIONS:
            rating += dfs(r + dr, c + dc, grid[r][c])
        
        return rating

    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += dfs(r, c, -1)
    
    return total_rating

print(part1("input.txt"))
print(part2("input.txt"))