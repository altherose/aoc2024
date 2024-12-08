with open("day1input.txt", "r") as file:
    input = file.read()

numbers = input.split()

list1 = []
list2 = []

for index, value in enumerate(numbers):
    if index % 2 == 0:
        list1.append(int(value))
    else:
        list2.append(int(value))

list1.sort()
list2.sort()

totalDifference = 0
similarityScore = 0

for index, value in enumerate(list1):
    diff = abs(value - list2[index])
    totalDifference += diff

    count = list2.count(value)
    similarityScore += (count*value)


print(f"Ans1 (Difference) = {totalDifference}")
print(f"Ans2 (Similarity) = {similarityScore}")






