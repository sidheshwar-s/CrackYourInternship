class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def bfs(node):
            visited.add(node)
            queue = deque([node])
            while queue:
                cur_node = queue.popleft()
                for neigh in graph[cur_node]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
                    
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
                bfs(node)
        
        return ans - 1