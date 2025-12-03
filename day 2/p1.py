from tqdm import tqdm

with open('out', 'r') as f:
    ranges = [list(map(int, i.split('-'))) for i in f.read().split(',')]

res = 0
for a, b in tqdm(ranges):
    for i in range(a, b + 1):
       j = str(i)
       if len(j) % 2 == 0 and j[:len(j) // 2] == j[len(j) // 2:]:
           res += i

print(res)