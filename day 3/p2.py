with open('out', 'r') as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    l, r = 0, len(line) - 11
    cur = ''
    for j in range(12):
        m, i = -1, -1
        for k in range(l, r):
            if m < int(line[k]):
                m = int(line[k])
                i = k
        l = i + 1
        r = len(line) - 10 + j
        cur += str(m)
    res += int(cur)

print(res)