from tqdm import tqdm

with open('out', 'r') as f:
    ranges = [list(map(int, i.split('-'))) for i in f.read().split(',')]

res = 0
for a, b in tqdm(ranges):
    for i in range(a, b + 1):
       j = str(i)
       for k in range(1, len(j)):
            if len(j) % k == 0 and j[:k] * (len(j) // k) == j:
                res += i
                break

print(res)