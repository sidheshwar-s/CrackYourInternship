class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		from collections import deque
		
		visited = [False] * V
		
		def check_cycle(node):
		    visited[node] = True
		    queue = deque([(node, -1)])
            while queue:
    		    node, parent = queue.popleft()
    		    for n in adj[node]:
    		        if not visited[n]:
    		            visited[n] = True
    		            queue.append((n, node))
    		        elif parent != n:
    		            return True
    		return False
    	
    	for n in range(V):
    	    if not visited[n]:
    	        if check_cycle(n): return True
    	
    	return False