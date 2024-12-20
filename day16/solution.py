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
    parents = {}

    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        r, c, dr, dc = node
        if grid[r][c] == 'E':
            return cost, parents

        # Go straight
        new_r = r + dr
        new_c = c + dc
        n1 = (new_r, new_c, dr, dc)
        if not_wall(new_r, new_c, grid):
            if (n1 not in est or (cost + 1) < est[n1]):
                est[n1] = cost + 1
                heapq.heappush(pq, (cost + 1, n1))
                parents[n1] = [node]
            elif (cost + 1) == est[n1]:
                parents[n1].append(node)

        # Turn left
        ldr, ldc = turn_left(dr, dc)
        n2 = (r, c, ldr, ldc)
        if n2 not in est or (cost + 1000) < est[n2]:
            est[n2] = cost + 1000
            heapq.heappush(pq, (cost + 1000, n2))
            parents[n2] = [node]
        elif (cost + 1000) == est[n2]:
            parents[n2].append(node)

        # Turn right
        rdr, rdc = turn_right(dr, dc)
        n3 = (r, c, rdr, rdc)
        if n3 not in est or (cost + 1000) < est[n3]:
            est[n3] = cost + 1000
            heapq.heappush(pq, (cost + 1000, n3))
            parents[n3] = [node]
        elif (cost + 1000) == est[n3]:
            parents[n3].append(node)

def part1(file):
    grid = read_input(file)
    start = get_start(grid)
    cost, _ = dijkstra(grid, start)

    return cost

def get_end_positions(grid, parents):
    rows, cols = len(grid), len(grid[0])
    
    end_positions = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'E':
                for dr, dc in DIRECTIONS:
                    node = (r, c, dr, dc)
                    if node in parents:
                        end_positions.append(node)
    
    return end_positions

def part2(file):
    grid = read_input(file)
    start = get_start(grid)
    _, parents = dijkstra(grid, start)
    best_path_tiles = set()

    def dfs(node):
        best_path_tiles.add((node[:2]))
        if node == start:
            return 
        for parent in parents[node]:
            dfs(parent)

    end_postions = get_end_positions(grid, parents)
    for end_position in end_postions:
        dfs(end_position)

    return len(best_path_tiles)

print(part1("input.txt"))
print(part2("input.txt"))