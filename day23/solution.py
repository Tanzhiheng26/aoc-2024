from collections import defaultdict
from itertools import combinations

def read_input(file):
    adj_list = defaultdict(set)
    with open(file, 'r') as f:
        for line in f:
            u, v = line.strip().split('-')
            adj_list[u].add(v)
            adj_list[v].add(u)
    return adj_list

def part1(file):
    adj_list = read_input(file)
    triplets = set()
    for k in adj_list:
        if k[0] == 't':
            pairs = combinations(adj_list[k], 2)
            for u, v in pairs:
                if u in adj_list[v]:
                    h = hash(k) + hash(u) + hash(v)
                    triplets.add(h)
    return len(triplets)

def is_clique(vertices, adj_list):
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if vertices[j] not in adj_list[vertices[i]]:
                return False
    return True

def part2(file):
    adj_list = read_input(file)
    max_degree = max([len(neighbors) for neighbors in adj_list.values()])
    n = max_degree
    while n >= 1:
        for k in adj_list:
            for combi in combinations(adj_list[k], n):
                if is_clique(combi, adj_list):
                    return ','.join(sorted([k] + list(combi)))
        n -= 1

print(part1("input.txt")) 
print(part2("input.txt"))
