from math import prod

with open('out', 'r') as f:
    data = f.read().splitlines()
    grid = [list(i) for i in data[:-1]]
    operations = data[-1].split()

rows, cols = len(grid), len(grid[0])
res = 0
p = len(operations) - 1
nums = []
for c in range(cols - 1, -1, -1):
    cur = ''
    for r in range(rows):
        cur += grid[r][c]

    try:
        cur = int(cur)
        nums.append(cur)
    except:
        if operations[p] == '+':
            res += sum(nums)
        else:
            res += prod(nums)
        nums = []
        p -= 1

if operations[p] == '+':
    res += sum(nums)
else:
    res += prod(nums)
print(res)
