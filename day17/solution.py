def read_input(file):
    input = []
    with open(file, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            input.append(line.strip().split(": ")[1])
    
    for i in range(3):
        input[i] = int(input[i])
    input[3] = list(map(int, input[3].split(',')))
    return input

def execute_program(a, b, c, program):
    ptr = 0
    output = []

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c

    while ptr < len(program) - 1:
        opcode = program[ptr]
        operand = program[ptr + 1]
        jumped = False
        
        if opcode == 0:
            # adv
            a //= (2 ** combo(operand))
        elif opcode == 1:
            # bxl
            b ^= operand
        elif opcode == 2:
            # bst
            b = combo(operand) % 8
        elif opcode == 3:
            # jnz
            if a != 0:
                ptr = operand
                jumped = True
        elif opcode == 4:
            # bxc
            b ^= c
        elif opcode == 5:
            # out
            output.append(combo(operand) % 8)
        elif opcode == 6:
            # bdv
            b = a // (2 ** combo(operand))
        elif opcode == 7:
            # cdv
            c = a // (2 ** combo(operand))

        if not jumped:
            ptr += 2     

    return output

def part1(file):
    a, b, c, program = read_input(file)
    output = execute_program(a, b, c, program)
    return ','.join(list(map(str, output)))

"""
Part 2
------
Program: 2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0

bst(4): b = a % 8. Last 3 bits of a.
bxl(1): b = b ^ 1
cdv(5): c = a // (2 ** b)
bxl(5): b = b ^ 5
bxc(5): b = b ^ c
adv(3): a = a // 8. Right shift a by 3.
out(5): output b % 8
jnz(0): jump to 1st instruction if a != 0
"""
# Based on https://www.reddit.com/r/adventofcode/comments/1hgo81r/2024_day_17_genuinely_enjoyed_this/
def part2(file):
    _, b, c, program = read_input(file)
    a_values = []
    no_jump = program[:-2]

    def dfs(a, i):
        if int(execute_program(a, b, c, no_jump)[0]) != program[i]:
            return 
        if i == 0:
            a_values.append(a)
            return 

        for next_3_bits in range(8):
            dfs(a * 8 + next_3_bits, i - 1)
    
    # a cannot be 0 at the start of the last iteration
    for a in range(1, 8):
        dfs(a, len(program) - 1)
    
    return min(a_values)

print(part1("input.txt"))
print(part2("input.txt"))
