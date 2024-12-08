with open("day5input.txt", "r") as file:
    input = file.read()

rules = input.split("\n\n")[0].splitlines()
updates = input.split("\n\n")[1].splitlines()

rules = [rule.split("|") for rule in rules]
rules = zip(*rules)
rulesPage1, rulesPage2 = list(rules)
rulesPage1 = [int(rule) for rule in rulesPage1]
rulesPage2 = [int(rule) for rule in rulesPage2]

correctUpdates = []

def checkUpdate(pages):
    remainingPages = pages
    for i in range(len(pages)):
       currentPage = remainingPages[0]
       remainingPages = remainingPages[1:]
       for index, value in enumerate(rulesPage2):
           if value == currentPage:
               for j, v in enumerate(remainingPages):
                   if v == rulesPage1[index]:
                       updatedPages = pages[:i] + [v] + [currentPage] + remainingPages[:j] + remainingPages[j+1:]
                       return False, updatedPages
    return True, pages

sumMiddleNumbers = 0
incorrectUpdates = []
correctUpdates = []

for update in updates:
    pages = update.split(",")
    pages = [int(page) for page in pages]
    if checkUpdate(pages)[0]:
        middleIndex = len(pages) // 2
        sumMiddleNumbers += pages[middleIndex]
        correctUpdates.append(update)
    else:
        incorrectUpdates.append(update)

print(sumMiddleNumbers)

# Part 2
def checkUpdateRecursive(pages):
    remainingPages = pages
    for i in range(len(pages)):
       currentPage = remainingPages[0]
       remainingPages = remainingPages[1:]
       for index, value in enumerate(rulesPage2):
           if value == currentPage:
               for j, v in enumerate(remainingPages):
                   if v == rulesPage1[index]:
                       updatedPages = pages[:i] + [v] + [currentPage] + remainingPages[:j] + remainingPages[j+1:]
                       return checkUpdateRecursive(updatedPages)
    return True, pages

sumMiddleNumbers = 0

for update in incorrectUpdates:
    pages = update.split(",")
    pages = [int(page) for page in pages]
    a, b = checkUpdateRecursive(pages)
    if a:
        sumMiddleNumbers += b[len(b) // 2]

print(sumMiddleNumbers)
