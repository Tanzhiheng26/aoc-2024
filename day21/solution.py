from collections import deque

numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', 'A']
]

directional_keypad = [
    ['', '^', 'A'],
    ['<', 'v', '>']
]

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
BUTTON = {
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<',
    (-1, 0): '^'
}

def read_input(file):
    codes = []
    with open(file, 'r') as f:
        for line in f:
            codes.append(line.strip())
    return codes

def inbounds(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != ''

def get_index(button, grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == button:
                return (r, c)

def bfs(start, end, keypad):
    if start == end:
        return ['A']

    start_index = get_index(start, keypad)
    q = deque([start_index])
    visited = {start_index}
    parent = {}

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS:
            next_r = r + dr
            next_c = c + dc
            if inbounds(next_r, next_c, keypad) and (next_r, next_c) not in visited:
                q.append((next_r, next_c))
                visited.add((next_r, next_c))        
                parent[(next_r, next_c)] = ((r, c), BUTTON[(dr, dc)])

                if keypad[next_r][next_c] == end:
                    moves = []
                    i = (next_r, next_c)
                    while i != start_index:
                        i, move = parent[i]
                        moves.append(move)
                    return moves[::-1] + ['A']

def get_moves(code, keypad):
    moves = []
    for i in range(len(code)):
        if i == 0:
            moves += bfs('A', code[i], keypad)
        else:
            moves += bfs(code[i - 1], code[i], keypad)
    return moves

def part1(file):
    codes = read_input(file)
    result = 0
    for code in codes:
        moves1 = get_moves(code, numeric_keypad)
        moves2 = get_moves(moves1, directional_keypad)
        moves3 = get_moves(moves2, directional_keypad)
        complexity = len(moves3) * int(code[:-1])
        result += complexity
    return result

print(part1("test.txt"))