from collections import defaultdict
import numpy as np

WIDTH = 101
HEIGHT = 103

def read_input(file):
    robots = []
    with open(file, 'r') as f:
        for line in f:
            p, v = line.split()
            px, py = map(int, p[2:].split(','))
            vx, vy = map(int, v[2:].split(','))
            robots.append((px, py, vx, vy))
    return robots

def position(robot, seconds):
    px, py, vx, vy = robot
    x = (px + seconds * vx) % WIDTH
    y = (py + seconds * vy) % HEIGHT
    return (x, y)

def part1(file):
    robots = read_input(file)
    count = defaultdict(int)
    for robot in robots:
        count[position(robot, 100)] += 1
    
    def quadrant_robots(x_start, x_end, y_start, y_end):
        robots = 0
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                robots += count[(x, y)]
        return robots
    
    q1 = quadrant_robots(0, (WIDTH - 1) // 2, 0, (HEIGHT - 1) // 2)
    q2 = quadrant_robots((WIDTH - 1) // 2 + 1, WIDTH, 0, (HEIGHT - 1) // 2)
    q3 = quadrant_robots(0, (WIDTH - 1) // 2, (HEIGHT - 1) // 2 + 1, HEIGHT)
    q4 = quadrant_robots((WIDTH - 1) // 2 + 1, WIDTH, (HEIGHT - 1) // 2 + 1, HEIGHT)

    return q1 * q2 * q3 * q4

def display_robots(robots, t):
    grid = [['.'] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        x, y = position(robot, t)
        grid[y][x] = '#'
    for i in range(HEIGHT):
        grid[i] = ''.join(grid[i])
    print('\n'.join(grid))

# Based on https://www.reddit.com/r/adventofcode/comments/1he0asr/2024_day_14_part_2_why_have_fun_with_image/
def part2(file):
    robots = read_input(file)
    
    x_var = []
    y_var = []
    for s in range(WIDTH):
        x_var.append(np.var([position(robot, s)[0] for robot in robots]))
    for s in range(HEIGHT):
        y_var.append(np.var([position(robot, s)[1] for robot in robots]))
    
    tx = np.argmin(x_var)
    ty = np.argmin(y_var)
    
    while tx % HEIGHT != ty:
        tx += WIDTH

    display_robots(robots, tx)
    return tx

print(part1("input.txt"))
print(part2("input.txt"))