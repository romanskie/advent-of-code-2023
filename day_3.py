import re
import math

inp = open('input/day_3.txt', 'r')
lines = inp.readlines()

special_char_pattern = r'[^A-Za-z0-9.\n]'
number_pattern = r'\d+'

def get_coordinate_range_per_number(lines): 
    ranges_per_number = {}
    for i, row in enumerate(lines):
        for m in re.finditer(number_pattern, row):
            key = m.group()
            value = set()
            for j in range(m.start(), m.end()):
                value.add((j, i))

            if key not in ranges_per_number:
                ranges_per_number[key] = [value]
            else:
                old_value = ranges_per_number[key]
                old_value += [value]
                ranges_per_number[key] = old_value

    return ranges_per_number

def is_special_char(c):
    return bool(re.match(special_char_pattern, c))

def get_neighbors(lines, i, j):
    M = len(lines)
    N = len(lines[i])
    neighbors = []
    if j-1 >= 0:
        neighbors.append((lines[i][j-1], (j-1, i)))
    if j+1 < N:
        neighbors.append((lines[i][j+1], (j+1, i)))
    if i-1 >= 0:
        neighbors.append((lines[i-1][j], (j, i-1)))
    if i+1 < M:
        neighbors.append((lines[i+1][j], (j, i+1)))
    if j-1 >= 0 and i-1 >= 0:
        neighbors.append((lines[i-1][j-1], (j-1, i-1)))
    if j-1 >= 0 and i+1 < M:
        neighbors.append((lines[i+1][j-1], (j-1, i+1)))
    if j+1 < N and i-1 >= 0:
        neighbors.append((lines[i-1][j+1], (j+1, i-1)))
    if j+1 < N and i+1 < M:
        neighbors.append((lines[i+1][j+1], (j+1, i+1)))
    return neighbors

def has_special_char_neighbor(lines, i, j):
    neighbors = get_neighbors(lines, i, j)
    for n in neighbors:
        s, _ = n
        if is_special_char(s):
            return True
    return False

def part1():
    coordinate_range_per_number = get_coordinate_range_per_number(lines)
    gear_ratios = []
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            number_match = re.match(number_pattern, col)
            if bool(number_match) and has_special_char_neighbor(lines, i, j):
                p = (j, i)
                for key, value in coordinate_range_per_number.items():
                    for idx, s in enumerate(value):
                        if p in s:
                            gear_ratios.append(int(key))
                            coordinate_range_per_number[key].pop(idx)
                            break;
    return sum(gear_ratios)

def part2():
    ranges_per_number = get_coordinate_range_per_number(lines)
    result = []
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            if col == "*":
                sub_result = []
                for n in get_neighbors(lines, i, j):
                    char, p = n
                    if char.isdigit():
                         for key, value in ranges_per_number.items():
                            for idx, s in enumerate(value):
                                if p in s:
                                    sub_result.append(int(key))
                                    ranges_per_number[key].pop(idx)
                                    break;
                if len(sub_result) > 1:
                    result.append(sub_result)

    gear_ratios = 0
    for sub in result:
        gear_ratios += math.prod(sub)
    return gear_ratios

print(part1()) #543867
print(part2()) #79613331