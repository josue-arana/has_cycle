# PROBLEM: 
# Given an  undirected graph G, determine if the graph is cyclic or acyclic.
# The graph is given as a list of lists where there is an edge between node i
# and node j if the list in index i contains the number j.  The graph contains
# nodes labeled 0,..., len(graph) - 1.

def has_cycle(graph):
	# print(graph) #prints for referrence

	#edge cases, check if the graph is empty 
	if graph is None or len(graph) == 0:
		return False

	#dictionary to keep track of visited and unvisited elements. 
	visited = {}

	#Inialize all indexes/vertices as not visited (false)
	for i in range(0,len(graph)):
		visited[i] = False


	#Auxiliary functino to traverse the graph using DFS recursively, taking the current node, the visited list, and the parent as paremeters
	def dfs(curr, visited, parent):
		# print("curr: ", curr, " parent ", parent)  #prints for referrence

		#check the current node to visited. 
		visited[curr] = True

		#visit each neighbor of each vertex in the graph
		for v in graph[curr]:

			#if the neighboor is not visited, then visit it. 
			if not visited[v]:
				#visit the next neighbor recursively.
				if dfs(v, visited, curr):
					return True

			#this checks if there is a cycle in the graph or not. 
			#if the next neightbor was already visited and is not the parent vertex, then we have a cycle.
			elif v != parent:
				return True

		#this is returned if there is no cycle found. 
		return False


	#Check every vertex inc ase the graph is disconnected.
	for u in range(0, len(graph)):
		if not visited[u]:
			if dfs(u, visited, -1):
				return True

	return False	


# Explanation: This algorthm consist of first checking the edge cases. If the given graph is None or empty, we return false.
# We then create a dictionary to keep track of visited and unvisited elements. Inialize all indexes/vertices as not visited (false)
# Then we use an auxiliary function to traverse the graph using DFS recursively, taking the current node, the visited list, and the parent as paremeters.
# In the loop, we first check if the current vertex to visited, this will prevent infinite recursion. Then if the current vertex is 
# not visited, we visit each neighbor of this, recursively.
# The key to check if there is a cycle in the graph is that when we are loocking for the next neighboor, if this was already visited 
# and the neighbor is not the parent of the node, we can say that we have a cycle. Similarly, if this is not true, we can say 
# that we do not have a graph. Lastly, we repeat the process for every single vertex in the graph, which will determine if there
# is a cycle even if the graph is disconnected. 

# Time Complexity: time complexity of dfs is O(V+E). Because this is an indirected graph we check each edge twice. 
#  therefore we have O(V) + O(2E) but overall this is ~ O(V + E).
# Space Complexity: We use a dictionary to store the vertices, not edges. O(V)
# By Josue Arana. 