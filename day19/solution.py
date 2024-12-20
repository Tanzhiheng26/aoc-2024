def read_input(file):
    with open(file, "r") as f:
        towels, designs = f.read().split("\n\n")
        towels = towels.split(', ')
        designs = designs.split('\n')
        return towels, designs

def prefix_match(towel, design):
    for i in range(len(towel)):
        if towel[i] != design[i]:
            return False
    return True

def part1(file):
    towels, designs = read_input(file)
        
    def dfs(towel, design, memo):
        if towel in memo:
            return memo[towel]
        if len(towel) > len(design) or not prefix_match(towel, design):
            return False
        if towel == design:
            return True
        
        for t in towels:
            if dfs(towel + t, design, memo):
                memo[towel] = True
                return True
        
        memo[towel] = False
        return False

    result = 0
    for design in designs:
        result += dfs("", design, {})
    return result

def part2(file):
    towels, designs = read_input(file)
        
    def dfs(towel, design, memo):
        if towel in memo:
            return memo[towel]
        if len(towel) > len(design) or not prefix_match(towel, design):
            return 0
        if towel == design:
            return 1
        
        ways = 0
        for t in towels:
            ways += dfs(towel + t, design, memo)
        memo[towel] = ways
        return ways

    result = 0
    for design in designs:
        result += dfs("", design, {})
    return result

print(part1("input.txt"))
print(part2("input.txt"))