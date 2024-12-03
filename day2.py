with open("day2input.txt", "r") as file:
    input = file.read()

def isSafe(levels):
    asc = (levels[1] - levels[0]) > 0
    for i in range(1, len(levels)):
        increment = levels[i] - levels[i-1]
        if abs(increment) not in [1, 2, 3]:
            return False
        elif (increment > 0) != asc:
            return False
        else:
            continue
    return True

safeReports = 0
safeDampedReports = 0

reports = input.splitlines()

for report in reports:
    levels = report.split()
    levels = [int(l) for l in levels]

    if isSafe(levels):
        safeReports += 1
    
    for index, value in enumerate(levels):
        dampedLevels = levels[:index] + levels[index+1:]
        if isSafe(dampedLevels):
            safeDampedReports += 1
            break

print(safeReports)
print(safeDampedReports)
    
