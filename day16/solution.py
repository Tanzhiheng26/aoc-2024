import heapq

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0)) # East, South, West, North

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def get_start(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                return (r, c, 0, 1)
            
def not_wall(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

def turn_left(dr, dc):
    i = DIRECTIONS.index((dr, dc))
    return DIRECTIONS[(i - 1) % 4]

def turn_right(dr, dc):
    i = DIRECTIONS.index((dr, dc))
    return DIRECTIONS[(i + 1) % 4]

def dijkstra(grid, start):
    est = {start: 0}
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        r, c, dr, dc = node
        if grid[r][c] == 'E':
            return cost

        # Go straight
        new_r = r + dr
        new_c = c + dc
        n1 = (new_r, new_c, dr, dc)
        if not_wall(new_r, new_c, grid) and (n1 not in est or (cost + 1) < est[n1]):
            est[n1] = cost + 1
            heapq.heappush(pq, (cost + 1, n1))

        # Turn left
        ldr, ldc = turn_left(dr, dc)
        n2 = (r, c, ldr, ldc)
        if n2 not in est or (cost + 1000) < est[n2]:
            est[n2] = cost + 1000
            heapq.heappush(pq, (cost + 1000, n2))

        # Turn right
        rdr, rdc = turn_right(dr, dc)
        n3 = (r, c, rdr, rdc)
        if n3 not in est or (cost + 1000) < est[n3]:
            est[n3] = cost + 1000
            heapq.heappush(pq, (cost + 1000, n3))

def part1(file):
    grid = read_input(file)
    start = get_start(grid)
    return dijkstra(grid, start)
        
print(part1("input.txt"))