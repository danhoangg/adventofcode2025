with open('out', 'r') as f:
    lines = f.read().split('\n')

res = 0
cur = 50
for l in lines:
    d = l[0]
    r = int(l[1:])

    if d == 'L':
        cur -= r
    else:
        cur += r
    cur %= 100

    if cur == 0:
        res += 1

print(res)