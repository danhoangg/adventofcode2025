with open('out', 'r') as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(grid[0])
res = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '@':
                    count += 1
            if count < 4:
                res += 1

print(res)