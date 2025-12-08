from collections import defaultdict
from math import sqrt
import heapq

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def mult_largest(self, n=3):
        count = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            count[root] += 1

        sizes = sorted(count.values(), reverse=True)
        res = 1
        for i in range(n):
            res *= sizes[i]
        return res


def euclidian_distance(a, b):
    return sqrt(sum([pow(abs(i - j), 2) for i, j in zip(a, b)]))


with open('out', 'r') as f:
    coords = [list(map(int, i.split(','))) for i in f.read().splitlines()]

pq = []
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        heapq.heappush(pq, (euclidian_distance(coords[i], coords[j]), i, j))

dsu = DisjointSetUnion(len(coords))
for i in range(1000):
    d, u, v = heapq.heappop(pq)
    dsu.union(u, v)

print(dsu.mult_largest())