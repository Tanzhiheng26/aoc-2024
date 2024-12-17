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
    
    return result

print(part1("input.txt"))