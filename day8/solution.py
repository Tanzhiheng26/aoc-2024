from collections import defaultdict

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def get_antinodes(antenna1, antenna2):
    r1, c1 = antenna1
    r2, c2 = antenna2
    antinode1 = (r1 + r1 - r2, c1 + c1 - c2)
    antinode2 = (r2 + r2 - r1, c2 + c2 - c1)
    return antinode1, antinode2

def inbounds(pos, grid):
    r, c = pos
    rows, cols = len(grid), len(grid[0]) 
    return 0 <= r < rows and 0 <= c < cols

def part1(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])
    antenna_pos = defaultdict(list)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                antenna_pos[grid[r][c]].append((r, c))
    
    antinodes = set()
    for positions in antenna_pos.values():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                antinode1, antinode2 = get_antinodes(positions[i], positions[j])
                if inbounds(antinode1, grid):
                    antinodes.add(antinode1)
                if inbounds(antinode2, grid):
                    antinodes.add(antinode2)

    return len(antinodes)

def part2(file):
    grid = read_input(file)
    rows, cols = len(grid), len(grid[0])
    antenna_pos = defaultdict(list)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                antenna_pos[grid[r][c]].append((r, c))
    
    antinodes = set()
    for positions in antenna_pos.values():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                dr1 = r1 - r2
                dc1 = c1 - c2
                dr2 = r2 - r1
                dc2 = c2 - c1

                while inbounds((r1, c1), grid):
                    antinodes.add((r1, c1))
                    r1 += dr1
                    c1 += dc1
                
                while inbounds((r2, c2), grid):
                    antinodes.add((r2, c2))
                    r2 += dr2
                    c2 += dc2

    return len(antinodes)

print(part1("input.txt"))
print(part2("input.txt"))