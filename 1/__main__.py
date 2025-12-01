
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
    full_turns = n // 100
    part = n % 100
    count += full_turns
    if d == "L":
        if pos != 0 and pos - part <= 0:
            count += 1
        pos = (pos - part) % 100
    elif d == "R":
        if pos != 0 and pos + part >= 100:
            count += 1
        pos = (pos + part) % 100

print(count)

