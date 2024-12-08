with open("day4input.txt", "r") as file:
    input = file.read()

grid = [list(row.strip()) for row in input.splitlines()]

word1 = "XMAS"
word2 = "MAS"
matches = 0
matches2 = 0

directions = [
    (0, 1), # across
    (1, 0), # down
    (0, -1), # back
    (-1, 0), # up
    (1, 1), # diagonal down right
    (1, -1), # diagonal down left
    (-1, -1), # diagnonal up left
    (-1, 1) # diagonal up right
]

rows = len(grid)
cols = len(grid[0])

def check(r, c, d, word):
    candidate = ""
    for i in range (len(word)):
        nr = r + (i * int(d[0]))
        nc = c + (i * int(d[1]))
        if 0 <= nr < rows and 0 <= nc < cols:
            candidate += grid[nr][nc]
        else:
            break
    return candidate == word

# Answer 1
for r in range(rows):
    for c in range(cols):
        for d in directions:
            if check (r, c, d, word1):
                matches += 1
                

# Answer 2 X-MAS
for r in range(rows):
    for c in range(cols):
        for d in directions:
            if check (r, c, d, word2):
                if d[0] == 0 or d[1] == 0: # only diagonals
                    continue
                else:
                    sd = (d[1], -d[0]) # vector rotate clockwise
                    sr = r + (d[0] - sd[0])
                    sc = c + (d[1] - sd[1])
                    if check(sr, sc, sd, word2):
                        matches2 += 1

print(matches)
print(matches2)

