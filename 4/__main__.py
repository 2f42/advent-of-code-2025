from collections import Counter

def count(grid):
    w = len(grid[0])
    h = len(grid)
    out = []
    for y, row in enumerate(grid):
        out.append([])
        for x, cell in enumerate(row):
            out[-1].append(0)
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue
                    if x+i-1 < 0 or x+i-1 >= w:
                        continue
                    if y+j-1 < 0 or y+j-1 >= h:
                        continue
                    if grid[y+j-1][x+i-1] >= 1 and grid[y][x] >= 1:
                        out[-1][-1] += 1
    t = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell >= 1 and out[y][x] < 4:
                t += 1
                out[y][x] = 0
                
    return t, out

grid = []
with open("./4/input.txt") as f:
    for row in (line.strip() for line in f.readlines()):
        grid.append([])
        for cell in row:
            grid[-1].append(1 if cell == "@" else 0)

t, o = count(grid)
print(t)
total = t
while t > 0:
    t, o = count(o)
    total += t
print(total)
