import time

with open("day6input.txt", "r") as file:
# with open("day6test.txt", "r") as file:
    input = file.read()

start_time = time.time()

rows = input.splitlines()
grid = [list(row) for row in rows]

obstacles = set()
start_direction = (-1, 0)
for i, row in enumerate(input.splitlines()):
    for j, col in enumerate(row):
        if col == "#":
            obstacles.add((i, j))
        elif col == "^":
            start_position = (i, j)
            
def inBounds(position):
    return position[0] >= 0 and position[0] < len(grid) and position[1] >= 0 and position[1] < len(grid[0])

def rotate(direction):
    return (direction[1], -direction[0])

def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def path_finder(obstacles):
    position = start_position
    direction = start_direction
    visited = set()
    visited.add((position, direction))
    while True:
        next_position = move(position, direction)
        if not inBounds(next_position):
            return False, visited
        elif (next_position, direction) in visited:
            return True, visited
        elif next_position in obstacles:
            direction = rotate(direction)
            visited.add((position, direction))
        else:
            position = next_position
            visited.add((position, direction))

def isValidObstacle(obstacle, valid_obstacles):
    return (
        inBounds(obstacle) 
        and obstacle not in obstacles 
        and obstacle != start_position 
        and obstacle not in valid_obstacles
    )

# Part 1
default_path = path_finder(obstacles)[1]
positions = set(pos for pos, _ in default_path)
print(len(positions))

# Part 2
valid_obstacles = set()
for position, direction in default_path:
    new_obstacle = move(position, direction)
    if not isValidObstacle(new_obstacle, valid_obstacles):
        continue
    new_obstacles = obstacles | {new_obstacle}
    if path_finder(new_obstacles)[0]:
        valid_obstacles.add(new_obstacle)

print(len(valid_obstacles))

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
    
