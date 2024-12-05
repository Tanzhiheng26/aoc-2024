from collections import defaultdict

def read_input(file):
    rules = []
    updates = []
    is_rule = True

    with open(file, "r") as f:
        for line in f:
            if line == '\n':
                is_rule = False
            elif is_rule:
                rule = list(map(int, line.strip().split('|')))
                rules.append(rule)
            else:
                update = list(map(int, line.strip().split(',')))
                updates.append(update)
            
    return rules, updates

def is_valid(update, rules):
    pages = set(update)
    page_index = { page: i for i, page in enumerate(update) }

    for rule in rules:
        u, v = rule
        rule_violated = u in pages and v in pages and page_index[u] > page_index[v]
        if rule_violated:
            return False
    
    return True

def part1(file):
    rules, updates = read_input(file)
    result = 0

    for update in updates:
        if is_valid(update, rules):
            result += update[len(update) // 2]
    
    return result

def get_relevant_rules(update, rules):
    pages = set(update)
    relevant_rules = []

    for rule in rules:
        u, v = rule
        if u in pages and v in pages:
            relevant_rules.append(rule)
    
    return relevant_rules

def create_adj_list(rules):
    adj_list = defaultdict(list)
    for u, v in rules:
        adj_list[u].append(v)
    return adj_list

def toposort(update, adj_list):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        for neighbor in adj_list[node]:
            dfs(neighbor)
        result.append(node)
        visited.add(node)
    
    for page in update:
        dfs(page)
    
    return result[::-1]

def part2(file):
    rules, updates = read_input(file)
    result = 0

    for update in updates:
        if is_valid(update, rules):
            continue
        relevant_rules = get_relevant_rules(update, rules)
        adj_list = create_adj_list(relevant_rules)
        ordered_update = toposort(update, adj_list)
        result += ordered_update[len(update) // 2]
    
    return result
        
                
print(part1("input.txt"))
print(part2("input.txt"))