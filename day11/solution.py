def read_input(file):
    with open(file, "r") as f:
        return list(map(int, f.read().split()))

def blink(stones):
    changed_stones = []
    for stone in stones:
        string = str(stone)
        if stone == 0:
            changed_stones.append(1)
        elif len(string) % 2 == 0:
            m = len(string) // 2
            left = int(string[:m])
            right = int(string[m:])
            changed_stones.append(left)
            changed_stones.append(right)
        else:
            changed_stones.append(stone * 2024)
    return changed_stones
            
def part1(file):
    stones = read_input(file)
    for _ in range(25):
        stones = blink(stones)
    return len(stones)

def part2(file):
    stones = read_input(file)
    memo = {}

    def dfs(stone, remaining_blinks):                
        if remaining_blinks == 0:
            return 1
        if (stone, remaining_blinks) in memo:
            return memo[(stone, remaining_blinks)]
        
        string = str(stone)
        if stone == 0:
            memo[(stone, remaining_blinks)] = dfs(1, remaining_blinks - 1)
        elif len(string) % 2 == 0:
            m = len(string) // 2
            left = int(string[:m])
            right = int(string[m:])
            memo[(stone, remaining_blinks)] = dfs(left, remaining_blinks - 1) + dfs(right, remaining_blinks - 1)
        else:
            memo[(stone, remaining_blinks)] = dfs(stone * 2024, remaining_blinks - 1)
        
        return memo[(stone, remaining_blinks)]
    
    result = 0
    for stone in stones:
        result += dfs(stone, 75)

    return result     

print(part1("input.txt"))
print(part2("input.txt"))