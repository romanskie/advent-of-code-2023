import re

inp = open('input/day_4.txt', 'r')
lines = inp.readlines()

WINNING_NUMBERS = 10

def get_matching_numbers_by_card_id():
    matching_numbers_by_card_id = {}
    for idx, line in enumerate(lines):
        card_id = idx + 1
        matches = re.findall(r'\d+', line)
        winning = { w : "" for w in matches[1:WINNING_NUMBERS + 1]}
        own = { o : "" for o in matches[WINNING_NUMBERS + 1:]}
        intersection = winning.keys() & own.keys()
        size = len(intersection)
        matching_numbers_by_card_id[card_id] = size
    return matching_numbers_by_card_id

def part1():
    points = 0
    matching_numbers_by_card_id = get_matching_numbers_by_card_id()
    for value in matching_numbers_by_card_id.values():
        points_per_card = 0 if value == 0 else 1
        for _ in range(value - 1):
            points_per_card = points_per_card * 2
        points += points_per_card
    return points

def part2():
    matching_numbers_by_card_id = get_matching_numbers_by_card_id()
    points = [1 for _ in matching_numbers_by_card_id]
    for i, p in enumerate(points):
        N = i + matching_numbers_by_card_id[i+1] + 1
        j = i+1
        while j < N:
            points[j] += p
            j += 1
    return sum(points)
    
        
print(part1())
print(part2())