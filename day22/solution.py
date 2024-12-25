from collections import deque

def read_input(file):
    secret_nums = []
    with open(file, 'r') as f:
        for line in f:
            secret_nums.append(int(line))
    return secret_nums

def next_num(num):
    mask = ((1 << 24) - 1) # 24 ones 
    num = ((num << 6) ^ num) & mask
    num = ((num >> 5) ^ num) & mask
    num = ((num << 11) ^ num) & mask
    return num

def part1(file):
    secret_nums = read_input(file)
    result = 0
    for num in secret_nums:
        for _ in range(2000):
            num = next_num(num)
        result += num
    return result

def part2(file):
    secret_nums = read_input(file)
    sequences = set()
    price_dicts = []

    for num in secret_nums:
        prev = num
        seq = deque()
        prices = {}
        for i in range(2000):
            num = next_num(num)
            diff = (num % 10) - (prev % 10)
            if i >= 4:
                seq.popleft()
            seq.append(diff)
            s = tuple(seq)
            sequences.add(s)
            if s not in prices:
                prices[s] = num % 10
            prev = num
        price_dicts.append(prices)
    
    max_bananas = 0
    for seq in sequences:
        bananas = 0
        for d in price_dicts:
            bananas += d.get(seq, 0)
        max_bananas = max(max_bananas, bananas)
    
    return max_bananas

print(part1("input.txt"))
print(part2("input.txt"))