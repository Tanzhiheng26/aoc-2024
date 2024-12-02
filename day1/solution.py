from collections import Counter

def read_input(file):
    left_list = []
    right_list = []
    
    with open(file, "r") as f:    
        for line in f:
            l, r = map(int, line.split())
            left_list.append(l)
            right_list.append(r)
        
    return left_list, right_list 

def part1(input_file):
    left_list, right_list = read_input(input_file)
    left_list.sort()
    right_list.sort()
    
    total_dist = 0
    for i in range(len(left_list)):
        dist = abs(left_list[i] - right_list[i])
        total_dist += dist
    
    return total_dist

def part2(input_file):
    left_list, right_list = read_input(input_file)
    left_counter = Counter(left_list)
    right_counter = Counter(right_list)
    
    total_score = 0
    for l, count in left_counter.items():
        score = l * right_counter[l] * count
        total_score += score

    return total_score

print("Part 1:", part1("input.txt"))
print("Part 2:", part2("input.txt"))