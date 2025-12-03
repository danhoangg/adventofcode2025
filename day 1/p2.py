with open('out', 'r') as f:
    lines = f.read().split('\n')

res = 0
cur = 50
for l in lines:
    d = l[0]
    r = int(l[1:])

    if d == 'R':
        f = (100 - cur) % 100
    else:
        f = cur % 100

    if f == 0:
        f = 100

    if r >= f:
        res += 1 + (r - f) // 100

    s = 1 if d == 'R' else -1
    cur = (cur + s * r) % 100

print(res)