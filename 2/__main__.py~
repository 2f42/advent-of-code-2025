def isvalid(n):
    digits = str(n)
    for i in range(1, len(digits)):
        if len(digits) % i != 0:
            continue
        reps = len(digits) // i
        substr = digits[:i]
        if substr * reps == digits:
            return False
    return True

ids = []
with open("./2/input.txt") as f:
    for start, end in (tuple(int(i) for i in r.split("-")) for r in f.read().strip().split(",")):
        ids.append((start, end))

total = 0
for start, end in ids:
    for i in range(start, end):
        if not isvalid(i):
            total += i

print(total)
