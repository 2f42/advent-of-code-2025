
combination = []
with open("./1/input.txt") as f:
    for line in f.readlines():
        l = line.strip()
        d = l[0]
        n = int(l[1:])
        combination.append((d, n))

pos = 50
count = 0
for d, n in combination:
    if d == "L":
        i = -1
    elif d == "R":
        i = 1

    for _ in range(n):
        pos = (pos + i) % 100
        if pos == 0:
            count += 1

print(count)

