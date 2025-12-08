with open('out', 'r') as f:
    grid = [list(i) for i in f.read().splitlines()]

rows, cols = len(grid), len(grid[0])

dp = [1] * cols
for r in range(rows-2, -1, -1):
    for c in range(cols):
        if grid[r][c] == '^':
            dp[c] = dp[c - 1] + dp[c + 1]

s = grid[0].index('S')
print(dp[s])