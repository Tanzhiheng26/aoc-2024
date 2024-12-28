def read_input(file):
    locks = []
    keys = []
    with open(file, 'r') as f:
        grids = f.read().split('\n\n')
        for grid in grids:
            heights = [0] * 5
            for row in grid.split('\n')[1:-1]:
                for i, col in enumerate(row):
                    if col == '#':
                        heights[i] += 1
            if grid[0] == '#':
                locks.append(heights)
            elif grid[0] == '.':
                keys.append(heights)
    return locks, keys

def part1(file):
    locks, keys = read_input(file)
    fitting_pairs = 0
    for lock in locks:
        for key in keys:
            overlap = False
            for i in range(len(lock)):
                if lock[i] + key[i] > 5:
                    overlap = True
            if not overlap:
                fitting_pairs += 1
    return fitting_pairs

print(part1("input.txt"))