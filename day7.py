import time
start_time = time.time()

with open("day7input.txt", "r") as file:
# with open("day7test.txt", "r") as file:
    input = file.read()

equations = input.splitlines()

def parse_equation(equation):
    left, right = equation.split(":")
    return int(left), [int(x) for x in right.strip().split(" ")]

def generate_combinations(items, n):
    if n == 0:
        return [[]] 
    smaller_combinations = generate_combinations(items, n - 1)
    result = []
    for combo in smaller_combinations:
        for item in items:
            result.append(combo + [item])
    return result

def test_equation(left, right, operators):
    combos = generate_combinations(operators, len(right)-1)
    for combo in combos:
        total = right[0]
        for i in range(len(combo)):
            if combo[i] == "*":
                total *= right[i+1]
            elif combo[i] == "+":
                total += right[i+1]
            elif combo[i] == "||":
                total = int(str(total) + str(right[i+1]))
            else:
                print("Invalid operator")
        if total == left:
            return True
    return False

# Part 1
results = []
for e in equations:
    left, right = parse_equation(e)
    operators = ["*", "+"]
    if test_equation(left, right, operators):
        results.append(left)
print(sum(results))

# Part 2
results = []
for e in equations:
    left, right = parse_equation(e)
    operators = ["*", "+", "||"]
    if test_equation(left, right, operators):
        results.append(left)
print(sum(results))


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
    
