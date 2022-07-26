class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
                    
        if n-1 > len(connections): return -1
        visited = set()
        ans = 0
        graph = defaultdict(list)
        
        for s, d in connections:    
            graph[s].append(d)
            graph[d].append(s)
        
        for node in range(n):
            if node not in visited:
                ans += 1
                dfs(node)
        
        return ans - 1