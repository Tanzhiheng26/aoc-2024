def read_input(file_name):
    reports = []
    with open(file_name, "r") as f:
        for line in f:
            report = list(map(int, line.split()))
            reports.append(report)
    return reports

def is_safe(report):
    if len(report) < 2:
        return True

    first_diff = report[1] - report[0]
    # all increasing -> all diff > 0
    # all decreasing -> all diff < 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3 and diff * first_diff > 0):
            return False
    
    return True

"""
Consider 3 levels: a b c

If a < b but b > c, should we remove b or c? Consider both.
1 4 2 3 (remove 4)
1 4 2 6 (remove 2)

Edge case: remove first element
1 4 3 2 
"""
def is_safe_with_removal(report):
    if len(report) < 2:
        return True

    first_diff = report[1] - report[0]
    # all increasing -> all diff > 0
    # all decreasing -> all diff < 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3 and diff * first_diff > 0):
            remove_curr = report[:i] + report[i + 1:] # remove report[i]
            remove_prev = report[:i - 1] + report[i:] # remove report[i - 1]
            remove_first = report[1:] # remove report[0]
            return is_safe(remove_curr) or is_safe(remove_prev) or is_safe(remove_first)
    
    return True

def part1(reports):
    return sum(map(is_safe, reports))

def part2(reports):
    return sum(map(is_safe_with_removal, reports))


reports = read_input("input.txt")
print("Part 1:", part1(reports))
print("Part 2:", part2(reports))