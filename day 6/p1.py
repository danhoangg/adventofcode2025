with open('out', 'r') as f:
    data = f.read().splitlines()
    grid = [list(map(int, i.split())) for i in data[:-1]]
    operations = data[-1].split()

rows, cols = len(grid), len(grid[0])
res = [0] * cols
for i in range(len(res)):
    if operations[i] == '*':
        res[i] = 1

for r in range(rows):
    for c in range(cols):
        res[c] = eval(str(res[c]) + operations[c] + str(grid[r][c]))

print(sum(res))
