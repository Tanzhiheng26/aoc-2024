import re
import numpy as np
import math

def parse_line(pattern, line):
    m = re.match(pattern, line)
    x = m.group(1)
    y = m.group(2)
    return x, y

def read_input(file):
    machines = []
    with open(file, "r") as f:
        for m in f.read().split("\n\n"):
            a, b, prize = m.split("\n")
            ax, ay = parse_line(r"Button A: X\+(\d+), Y\+(\d+)", a)
            bx, by = parse_line(r"Button B: X\+(\d+), Y\+(\d+)", b)
            px, py = parse_line(r"Prize: X=(\d+), Y=(\d+)", prize)
            machine = list(map(int, (ax, ay, bx, by, px, py)))
            machines.append(machine)
    return machines

def part1(file):
    machines = read_input(file)

    def dfs(x, y, ax, ay, bx, by, memo):
        if x == 0 and y == 0:
            return 0
        if x < 0 or y < 0:
            return float('inf')
        if (x, y) in memo:
            return memo[(x, y)]
        
        push_a = 3 + dfs(x - ax, y - ay, ax, ay, bx, by, memo)
        push_b = 1 + dfs(x - bx, y - by, ax, ay, bx, by, memo)
        memo[(x, y)] = min(push_a, push_b)
        
        return memo[(x, y)]

    total_tokens = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        tokens = dfs(px, py, ax, ay, bx, by, {})
        if tokens != float('inf'):
            total_tokens += tokens
    
    return total_tokens

def part2(file):
    machines = read_input(file)
    total_tokens = 0

    for machine in machines:
        ax, ay, bx, by, px, py = machine
        px += 10000000000000
        py += 10000000000000
        A = np.array([[ax, bx], [ay, by]])
        b = np.array([[px], [py]])
        x = np.linalg.solve(A, b)
                
        a_presses = round(x[0][0])
        b_presses = round(x[1][0])
        if (a_presses * ax + b_presses * bx) == px and (a_presses * ay + b_presses * by) == py:
            tokens = 3 * a_presses + b_presses
            total_tokens += tokens
    
    return total_tokens


print(part1("input.txt"))
print(part2("input.txt"))