with open('out', 'r') as f:
    sections = f.read().split('\n\n')

ranges = [list(map(int, i.split('-'))) for i in sections[0].splitlines()]
ranges.sort(key=lambda x: x[0])

last = -1
res = 0
for l, r in ranges:
    if l > last:
        res += r - l + 1
        last = r
    else:
        res += max(0, r - last)
        last = max(last, r)

print(res)