from collections import deque

DIRECTIONS = {
    '>': (0, 1), 
    'v': (1, 0), 
    '<': (0, -1), 
    '^': (-1, 0)
}

def read_input(file):
    with open(file, "r") as f:
        pos, moves = f.read().split('\n\n')
    grid = list(map(list, pos.split()))
    moves = moves.replace('\n', '')
    return grid, moves

def get_start(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                return (r, c)

def print_grid(grid):
    for r in range(len(grid)):
        grid[r] = ''.join(grid[r])
    print("\n".join(grid))

def part1(file):
    grid, moves = read_input(file)
    r, c = get_start(grid)
    grid[r][c] = '.'
    
    for move in moves:
        dr, dc = DIRECTIONS[move]
        next_r = r + dr
        next_c = c + dc

        if grid[next_r][next_c] == 'O':
            i = next_r
            j = next_c
            while grid[i][j] == 'O':
                i += dr
                j += dc
            if grid[i][j] == '.':
                grid[i][j] = 'O'
                grid[next_r][next_c] = '.'
        
        if grid[next_r][next_c] == '.':
            r = next_r
            c = next_c

    result = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                result += (100 * r + c)
    
    # print_grid(grid)
    return result


def expand(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            if grid[r][c] == '#':
                new_row.append('#')
                new_row.append('#')
            elif grid[r][c] == 'O':
                new_row.append('[')
                new_row.append(']')
            elif grid[r][c] == '.':
                new_row.append('.')
                new_row.append('.')
            elif grid[r][c] == '@':
                new_row.append('@')
                new_row.append('.')
        new_grid.append(new_row)
    return new_grid

def flip(p):
    return ']' if p == '[' else '['

def move_horizontally(r, c, move, grid):
    dc = DIRECTIONS[move][1]
    next_c = c + dc

    if grid[r][next_c] in ('[', ']'):
        i = next_c
        while grid[r][i] in ('[', ']'):
            i += dc
        if grid[r][i] == '.':
            for j in range(next_c + dc, i, dc):
                grid[r][j] = flip(grid[r][j])
            grid[r][i] = flip(grid[r][next_c])
            grid[r][next_c] = '.'
    
    if grid[r][next_c] == '.':
        return r, next_c
    else:
        return r, c

def move_vertically(r, c, move, grid):
    dr = DIRECTIONS[move][0]
    next_r = r + dr

    if grid[next_r][c] in ('[', ']'):
        box = (next_r, c, c + 1) if grid[next_r][c] == '[' else (next_r, c - 1, c)
        q = deque([box])
        can_move = True
        visited = []

        while q:
            for _ in range(len(q)):
                r1, c1, c2 = q.popleft()
                visited.append((r1, c1, c2))

                for i in range(c1 - 1, c2 + 1):
                    if grid[r1 + dr][i] == '[' and grid[r1 + dr][i + 1] == ']':
                        q.append((r1 + dr, i, i + 1))
                
                if grid[r1 + dr][c1] == '#' or grid[r1 + dr][c2] == '#':
                    can_move = False
        
        if can_move:
            for r1, c1, c2 in visited[::-1]:
                grid[r1 + dr][c1] = '['
                grid[r1 + dr][c2] = ']'
                grid[r1][c1] = '.'
                grid[r1][c2] = '.'

    if grid[next_r][c] == '.':
        return next_r, c
    else:
        return r, c

def part2(file):
    grid, moves = read_input(file)
    grid = expand(grid)
    r, c = get_start(grid)
    grid[r][c] = '.'

    for move in moves:
        if move in ('>',  '<'):
            r, c = move_horizontally(r, c, move, grid)
        else:
            r, c = move_vertically(r, c, move, grid)

    result = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '[':
                result += (100 * r + c)
    
    # print_grid(grid)
    return result
    

print(part1("input.txt"))
print(part2("input.txt"))