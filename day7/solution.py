import math

def read_input(file):
    equations = []
    with open(file, 'r') as f:
        for line in f:
            result, operands = line.split(": ")
            result = int(result)
            operands = list(map(int, operands.split()))
            equations.append([result, operands])
    return equations

def is_valid1(equation):
    result, operands = equation
    memo = {}

    def dfs(i, value):
        if (i, value) in memo:
            return memo[(i, value)]
        
        # calculate answer and memoize
        if i == len(operands):
            memo[(i, value)] = value == result
        elif value > result:
            memo[(i, value)] = False
        else:    
            memo[(i, value)] = dfs(i + 1, value + operands[i]) or dfs(i + 1, value * operands[i])

        return memo[(i, value)]

    return dfs(1, operands[0])

def part1(file):
    equations = read_input(file)
    result = 0

    for equation in equations:
        if is_valid1(equation):
            result += equation[0]
    
    return result

def concat(x, y):
    y_digits = int(math.log10(y)) + 1
    return x * 10**y_digits + y

def is_valid2(equation):
    result, operands = equation
    memo = {}

    def dfs(i, value):
        if (i, value) in memo:
            return memo[(i, value)]
        
        # calculate answer and memoize
        if i == len(operands):
            memo[(i, value)] = value == result
        elif value > result:
            memo[(i, value)] = False
        else:    
            memo[(i, value)] = dfs(i + 1, value + operands[i]) \
                            or dfs(i + 1, value * operands[i]) \
                            or dfs(i + 1, concat(value, operands[i]))

        return memo[(i, value)]

    return dfs(1, operands[0])

def part2(file):
    equations = read_input(file)
    result = 0

    for equation in equations:
        if is_valid2(equation):
            result += equation[0]
    
    return result

print(part1("input.txt"))
print(part2("input.txt"))