import re
inp = open('input/01.txt', 'r')
lines = inp.readlines()

digits = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6", 
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

#"eighthree  => 83
#"sevenine" => 79
pattern=r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"
result = 0
for line in lines:
    matches = re.findall(pattern, line)
    for idx, m in enumerate(matches):
        if m in digits:
            matches[idx] = digits[m]
    number = int(matches[0] + matches[-1])
    result += int(number)

print(result)
