import re

def read_input(file):
    with open(file, "r") as f:
        return f.read()

def find_instructions(pattern, input):
    return re.findall(pattern, input)

def mul(x, y):
    return x * y

def eval_instructions(instructions):
    return sum(map(eval, instructions))

def part1(file):
    input = read_input(file)
    pattern = r"mul\(\d+,\d+\)"
    instructions = find_instructions(pattern, input)
    return eval_instructions(instructions)

def part2(file):
    input = read_input(file)
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    instructions = find_instructions(pattern, input)
    
    result = 0
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            result += eval(instruction)
    return result

print(part1("input.txt"))
print(part2("input.txt"))