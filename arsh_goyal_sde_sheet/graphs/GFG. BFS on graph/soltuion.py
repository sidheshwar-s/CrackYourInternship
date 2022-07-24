class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        from collections import deque
        visited = set()
        ans = []
        queue = deque([0])
        while queue:
            node = queue.popleft()
            ans.append(node)
            visited.add(node)
            for v in adj[node]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
        return ans