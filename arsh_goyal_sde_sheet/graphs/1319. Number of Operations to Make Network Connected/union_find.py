class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
    
    def find(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return 0
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        N = len(connections)
        if N < n-1: return -1
        graph = UnionFind(n)
        for s,d in connections:
            graph.union(s, d)
        return sum(graph.find(s) == s for s in range(n)) - 1