class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    def find_cycle(node, par):
	        for n in adj[node]:
	            if n not in visited:
                    visited.add(n)
                    if find_cycle(n, node): return True
                elif n != par:
                    return True
            return False
            
        visited = set()
        for n in range(V):
            if n not in visited:
                visited.add(n)
                if find_cycle(n, -1):
                    return True
        
        return False