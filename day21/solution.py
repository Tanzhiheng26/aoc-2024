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
    
    vertical_moves = ()
    horizontal_moves = ()
    if dr > 0:
        vertical_moves = ('v',) * abs(dr)
    elif dr < 0:
        vertical_moves = ('^',) * abs(dr)
    
    if dc > 0:
        horizontal_moves = ('>',) * abs(dc)
    elif dc < 0:
        horizontal_moves = ('<',) * abs(dc)
    
    paths = set()
    if inbounds(start_r + dr, start_c, keypad):
        paths.add(vertical_moves + horizontal_moves + ('A',))
    if inbounds(start_r, start_c + dc, keypad):
        paths.add(horizontal_moves + vertical_moves + ('A',))
    
    return paths

def get_sequences(output, keypad):
    sequences = []

    def dfs(i, seq):
        if i == len(output):
            sequences.append(seq)
            return

        paths = get_paths('A', output[i], keypad) if i == 0 else get_paths(output[i - 1], output[i], keypad)
        for p in paths:
            dfs(i + 1, seq + p)
    
    dfs(0, ())
    return sequences

def part1(file):
    codes = read_input(file)
    result = 0
    for code in codes:
        seq1 = get_sequences(code, numeric_keypad)
        seq2 = []
        for seq in seq1:
            seq2 += get_sequences(seq, directional_keypad)
        seq3 = []
        for seq in seq2:
            seq3 += get_sequences(seq, directional_keypad)
        
        complexity = min(map(len, seq3)) * int(code[:-1])
        result += complexity
    return result

print(part1("input.txt"))