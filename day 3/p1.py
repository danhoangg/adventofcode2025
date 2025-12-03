with open('out', 'r') as f:
    lines = f.read().splitlines()

res = 0
for l in lines:
    p, q = 0, 1
    cur = int(l[p] + l[q])
    while q < len(l):
        cur = max(cur, int(l[p] + l[q]))
        if int(l[q]) > int(l[p]):
            p = q
        q += 1
    res += cur

print(res)