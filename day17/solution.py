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

print(part1("input.txt"))