from functools import cache

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

def get_paths(start, end, keypad):
    start_r, start_c = get_index(start, keypad)
    end_r, end_c = get_index(end, keypad)
    dr = end_r - start_r
    dc = end_c - start_c
    
    vertical_moves = ''
    horizontal_moves = ''
    if dr > 0:
        vertical_moves = 'v' * abs(dr)
    elif dr < 0:
        vertical_moves = '^' * abs(dr)
    
    if dc > 0:
        horizontal_moves = '>' * abs(dc)
    elif dc < 0:
        horizontal_moves = '<' * abs(dc)
    
    paths = set()
    if inbounds(start_r + dr, start_c, keypad):
        paths.add(vertical_moves + horizontal_moves + 'A')
    if inbounds(start_r, start_c + dc, keypad):
        paths.add(horizontal_moves + vertical_moves + 'A')
    
    return paths

def get_sequences(output, keypad):
    sequences = []

    def helper(i, seq):
        if i == len(output):
            sequences.append(seq)
            return

        paths = get_paths('A', output[i], keypad) if i == 0 else get_paths(output[i - 1], output[i], keypad)
        for p in paths:
            helper(i + 1, seq + p)
    
    helper(0, '')
    return sequences

def part1(file):
    codes = read_input(file)
    result = 0
    for code in codes:
        sequences = get_sequences(code, numeric_keypad)

        for _ in range(2):
            next_sequences = []
            for seq in sequences:
                next_sequences += get_sequences(seq, directional_keypad)
            sequences = next_sequences
        
        complexity = min(map(len, sequences)) * int(code[:-1])
        result += complexity
    return result

print(part1("input.txt"))


MAX_LEVEL = 26

# Based on https://www.reddit.com/r/adventofcode/comments/1hjx0x4/2024_day_21_quick_tutorial_to_solve_part_2_in/
# Because every input sequence returns to 'A' we can split them up and evaluate them separately.
@cache
def dfs(part, level):
    if level == 0:
        return len(part)
    
    sequences = get_sequences(part, numeric_keypad) if level == MAX_LEVEL else get_sequences(part, directional_keypad)
    result = float('inf')
    for sequence in sequences:
        parts = sequence.split('A')[:-1]
        total = 0
        for part in parts:
            total += dfs(part + 'A', level - 1)
        result = min(result, total)
    
    return result


def part2(file):
    codes = read_input(file)
    result = 0
    for code in codes:
        min_length = dfs(code, MAX_LEVEL)
        complexity = min_length * int(code[:-1])
        result += complexity
    return result

print(part2("input.txt"))
