import re
inp = open('input/day_2.txt', 'r')
lines = inp.readlines()

gameId_pattern = r'(?<=Game\s)\d+'
rgb_pattern = r'(\d+)(?=\s(blue|red|green))'

def filterValidSubsets(subset):
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    (number, colour) = subset
    return int(number) <= bag[colour]

def part_1():
    result = 0
    for line in lines:
        game_id = int(re.findall(gameId_pattern, line)[0])
        matches = re.findall(rgb_pattern, line)
        filtered = list(filter(filterValidSubsets, matches))
        result = result + game_id if filtered == matches else result
    return result


#[('3', 'blue'), ('4', 'red'), ('1', 'red'), ('2', 'green'), ('6', 'blue'), ('2', 'green')]
def part_2():
    result = 0
    for line in lines:
        cache = {}
        product = 1
        matches = re.findall(rgb_pattern, line)
        for match in matches:
            (value, key) = match
            if key not in cache:
                cache[key] = int(value)
            else:
                cache[key] = max(cache[key], int(value))
        for key in cache:
            product *= cache[key]
        result += product
    return result

print(part_1())
print(part_2())


