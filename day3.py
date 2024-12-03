import re

with open("day3input.txt", "r") as file:
    input = file.read()

total1 = 0
total2 = 0
enabled = True

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = re.findall(pattern, input)

for m in matches:
    if m =="do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    else:
        pattern = r"(\d{1,3}),(\d{1,3})"
        match = re.search(pattern, m)
        a = int(match.group(1))
        b = int(match.group(2))
        product = a * b
        total1 += product
        if enabled:
            total2 += product

print(f"Answer 1 = {total1}")
print(f"Answer 2 = {total2}")