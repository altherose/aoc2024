with open("day6input.txt", "r") as file:
# with open("day6test.txt", "r") as file:
    input = file.read()

rows = input.splitlines()
grid = [list(row) for row in rows]

start_direction = (-1, 0)
start_obstacles = []
path = []

for row_index, row in enumerate(input.splitlines()):
    for col_index, col in enumerate(row):
        if col == "#":
            start_obstacles.append((row_index, col_index))
        elif col == "^":
            start_position = (row_index, col_index)
            
def inBounds(position):
    return position[0] >= 0 and position[0] < len(grid) and position[1] >= 0 and position[1] < len(grid[0])

def rotate(direction):
    return (direction[1], -direction[0])

def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

# Part 1
position = start_position
direction = start_direction
path.append((position, direction))
while True:
    next_position = move(position, direction)
    if not inBounds(next_position):
        break
    elif next_position in start_obstacles:
        direction = rotate(direction)
        path.append((position, direction))
    else:
        position = next_position
        path.append((position, direction))
        
unique_path = []
for p in path:
    if p[0] not in unique_path:
        unique_path.append(p[0])

print(len(unique_path))

# Part 2

def test_obstacle(i, j):
    obstacles = []
    obstacles = start_obstacles + [(i, j)]  
    path = []
    position = start_position
    direction = start_direction
    path.append((position, direction))

    while True:
        next_position = move(position, direction)
        if (next_position, direction) in path:
            return True
        elif not inBounds(next_position):
            return False
        elif next_position in obstacles:
            direction = rotate(direction)
            path.append((position, direction))
        else:
            position = next_position
            path.append((position, direction))  

count = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "^" or col == "#":
            continue
        else:
            print(f"Testing {i}, {j}")
            if test_obstacle(i, j):
                count += 1
print(count)

