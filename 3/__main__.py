def max_joltage(bank, d):
    if d == 1:
        return max(bank)
    
    mj = 0
    mi = -1
    for i, j in enumerate(bank[:-d+1]):
        if j > mj:
            mj = j
            mi = i

    mj2 = max_joltage(bank[mi+1:], d-1)

    return mj * 10 ** (d-1) + mj2



banks = []
with open("./3/input.txt") as f:
    for bank in (line.strip() for line in f.readlines()):
        banks.append([int(i) for i in bank])

print(sum(max_joltage(b, 12) for b in banks))

