with open('out', 'r') as f:
    grid = [list(i) for i in f.read().splitlines()]

s = grid[0].index('S')

# wait i misread the question to how many tachyon beams end up at the end
# so now im just restructuring the solution
rows, cols = len(grid), len(grid[0])
visited = set()
res = [0]
def dfs(r, c):
    if (r, c) in visited:
        return
    if r >= rows:
        return

    visited.add((r, c))

    if grid[r][c] == '^':
        res[0] += 1
        if c + 1 < cols:
            dfs(r, c + 1)
        if c - 1 >= 0:
            dfs(r, c - 1)
    else:
        dfs(r + 1, c)


dfs(0, s)
print(res[0])