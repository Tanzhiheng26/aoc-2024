from collections import deque

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
ROWS = COLS = 71

def read_input(file):
    corrupted = []
    with open(file, 'r') as f:
        for line in f:
            coordinate = list(map(int, line.split(',')))
            corrupted.append(coordinate)
    return corrupted

def inbounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def generate_grid(n, corrupted):
    grid = [['.'] * COLS for _ in range(ROWS)]
    for i in range(n):
        x, y = corrupted[i]
        grid[y][x] = '#'
    return grid

def bfs(grid):
    visited = {(0, 0)}
    q = deque([(0, 0)])
    steps = 0

    while q:
        steps += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                next_r = r + dr
                next_c = c + dc
                if next_r == (ROWS - 1) and next_c == (COLS - 1):
                    return steps
                if inbounds(next_r, next_c) and grid[next_r][next_c] == '.' and (next_r, next_c) not in visited:
                    q.append((next_r, next_c))
                    visited.add((next_r, next_c))

    return -1

def part1(file):
    corrupted = read_input(file)
    grid = generate_grid(1024, corrupted)
    
    return bfs(grid)

def part2(file):
    corrupted = read_input(file)
    
    l, r = 1, len(corrupted)
    while l < r:
        m = (l + r) // 2
        grid = generate_grid(m, corrupted)
        
        can_exit = bfs(grid) != -1 
        if can_exit:
            l = m + 1
        else:
            r = m
    
    return corrupted[l - 1]


print(part1("input.txt"))
print(part2("input.txt"))
