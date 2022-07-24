class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = set()
        result = []
        def dfs(node):
            if node in visited:
                return  
            visited.add(node)
            result.append(node)
            for n in adj[node]:
                dfs(n)
        dfs(0)
        return result