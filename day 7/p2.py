with open('out', 'r') as f:
    grid = [list(i) for i in f.read().splitlines()]

s = grid[0].index('S')

# holy guess, conveniently setup for part 2
rows, cols = len(grid), len(grid[0])
visited = {}
def dfs(r, c):
    if (r, c) in visited:
        return visited[(r, c)]
    if r >= rows:
        return 1

    if grid[r][c] == '^':
        res = 0
        if c + 1 < cols:
            res += dfs(r, c + 1)
        if c - 1 >= 0:
            res += dfs(r, c - 1)

        visited[(r, c)] = res
        return res
    else:
        visited[(r, c)] = dfs(r + 1, c)
        return visited[(r, c)]


print(dfs(0, s))
