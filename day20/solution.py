from collections import deque

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

def read_input(file):
    grid = []
    with open(file, 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def get_start(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                return (r, c)

def inbounds(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def find_path(grid):
    # There is only a single path from the start to the end
    path_num = {}
    visited = set()

    r, c = get_start(grid)
    i = 0
    while grid[r][c] != 'E':
        path_num[(r, c)] = i
        visited.add((r, c))
        for dr, dc in DIRECTIONS:
            next_r = r + dr
            next_c = c + dc
            if grid[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                r = next_r
                c = next_c
                break
        i += 1
    path_num[(r, c)] = i

    return path_num

def part1(file):
    grid = read_input(file)
    path_num = find_path(grid)

    result = 0
    for r, c in path_num:
        # cheats are uniquely identified by their start position and end position
        end_pos = set()
        for dr, dc in DIRECTIONS:
            next_r = r + dr
            next_c = c + dc
            if grid[next_r][next_c] == '#':
                for dr, dc in DIRECTIONS:
                    end_r = next_r + dr
                    end_c = next_c + dc
                    if inbounds(end_r, end_c, grid) and grid[end_r][end_c] != '#':
                        saved = path_num[(end_r, end_c)] - (path_num[(r, c)] + 2)
                        if saved >= 100:
                            end_pos.add((end_r, end_c))
        result += len(end_pos)

    return result

# Using hint from reddit
# https://www.reddit.com/r/adventofcode/comments/1hihdbj/comment/m2z0c5r/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def part2(file):
    grid = read_input(file)
    path_num = find_path(grid)

    result = 0
    for r, c in path_num:
        for dr in range(-20, 21):
            max_dc = 20 - abs(dr)
            for dc in range(-max_dc, max_dc + 1):
                end_r = r + dr
                end_c = c + dc
                if inbounds(end_r, end_c, grid) and grid[end_r][end_c] != '#':
                    manhattan_dist = abs(dr) + abs(dc)
                    saved = path_num[(end_r, end_c)] - (path_num[(r, c)] + manhattan_dist)
                    if saved >= 100:
                        result += 1

    return result

print(part1("input.txt"))
print(part2("input.txt"))