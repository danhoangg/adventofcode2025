with open('out', 'r') as f:
    sections = f.read().split('\n\n')

ranges = [list(map(int, i.split('-'))) for i in sections[0].splitlines()]
ids = list(map(int, sections[1].splitlines()))

res = 0
for i in ids:
    for l, r in ranges:
        if l <= i <= r:
            res += 1
            break

print(res)