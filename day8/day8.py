import time
start_time = time.time()

with open("input.txt", "r") as file:
# with open("test.txt", "r") as file:
    input = file.read()

grid = [list(row) for row in input.splitlines()]
antennas = {}
antinodes = set()
all_antinodes = set()

def get_pairs(coords):
    pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            pairs.append((coords[i], coords[j]))
    return pairs

def inBounds(coord):
    return coord[0] >= 0 and coord[0] < len(grid) and coord[1] >= 0 and coord[1] < len(grid[coord[0]])

def add_antinode(pair):
    a = pair[0]
    b = pair[1]
    offset = (a[0] - b[0], a[1] - b[1])
    antinode = (a[0] + offset[0], a[1] + offset[1])
    if inBounds(antinode):
        antinodes.add(antinode)

def add_all_antinodes(pair):
    a = pair[0]
    b = pair[1]
    offset = (a[0] - b[0], a[1] - b[1])
    while True:
        if inBounds(a):
            all_antinodes.add(a)
            a= (a[0] + offset[0], a[1] + offset[1])
        else:
            break

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != ".":
            freq = grid[r][c]
            if freq not in antennas:
                antennas[freq] = []
            antennas[freq].append((r, c))
    
for freq in antennas:
    pairs = get_pairs(antennas[freq])
    for pair in pairs:
        add_antinode((pair[0], pair[1]))
        add_antinode((pair[1], pair[0]))
        add_all_antinodes((pair[0], pair[1]))
        add_all_antinodes((pair[1], pair[0]))

print(len(antinodes))
print(len(all_antinodes))