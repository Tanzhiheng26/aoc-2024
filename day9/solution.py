import math

def read_input(file):
    with open(file, 'r') as f:
        return f.read()

def get_blocks1(disk_map):
    blocks = []
    free_spaces = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            file_length = int(disk_map[i])
            id = i // 2
            for _ in range(file_length):
                blocks.append(id)
        else:
            free_space = int(disk_map[i])
            for _ in range(free_space):
                blocks.append('.')
                free_spaces.append(len(blocks) - 1)
    return blocks, free_spaces

def calc_checksum1(blocks):
    checksum = 0
    for i, id in enumerate(blocks):
        if id == '.':
            break
        checksum += (i * id)
    return checksum

def part1(file):
    disk_map = read_input(file)
    blocks, free_spaces = get_blocks1(disk_map)
    j = 0
    for i in range(len(blocks) - 1, -1, -1):
        if free_spaces[j] >= i:
            break
        if blocks[i] == '.':
            continue
        blocks[free_spaces[j]] = blocks[i]
        blocks[i] = '.'
        j += 1
    return calc_checksum1(blocks)

def get_blocks2(disk_map):
    blocks = []
    free_spaces = []
    files = []

    for i in range(len(disk_map)):
        if i % 2 == 0:
            file_start = len(blocks)
            file_length = int(disk_map[i])
            files.append((file_start, file_length))
            
            id = i // 2
            for _ in range(file_length):
                blocks.append(id)
        else:
            free_start = len(blocks)
            free_length = int(disk_map[i])
            free_spaces.append((free_start, free_length))
            
            for _ in range(free_length):
                blocks.append('.')
                
    return blocks, free_spaces, files

def move_file(id, file_start, file_length, free_start, blocks):
    for i in range(free_start, free_start + file_length):
        blocks[i] = id
    for i in range(file_start, file_start + file_length):
        blocks[i] = '.'
    return blocks

def calc_checksum2(blocks):
    checksum = 0
    for i, id in enumerate(blocks):
        if id == '.':
            continue
        checksum += (i * id)
    return checksum

def part2(file):
    disk_map = read_input(file)
    blocks, free_spaces, files = get_blocks2(disk_map)

    for id in range(len(files) - 1, -1, -1):
        file_start, file_length = files[id]
        
        leftover_start = -1
        leftover_length = 0
        modified_index = -1

        for i, free_space in enumerate(free_spaces):
            free_start, free_length = free_space
            if free_start >= file_start:
                break
            if free_length >= file_length:
                move_file(id, file_start, file_length, free_start, blocks)
                leftover_length = free_length - file_length
                leftover_start = free_start + file_length
                modified_index = i
                break
        
        if modified_index >= 0:
            free_spaces[modified_index] = (leftover_start, leftover_length)
            
    return calc_checksum2(blocks)

print(part1("input.txt"))
print(part2("input.txt"))