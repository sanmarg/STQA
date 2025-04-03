# Python: DFS & BFS in Graph
class Graph:
    def __init__(self, vertices):
        self.V= vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v]= True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if visited[neighbor] == False: # '==' instead of 'is False'
                self.dfs_util(neighbor, visited)

    def DFS(self, start):
        visited= [False] * self.V
        self.dfs_util(start, visited)

    def BFS(self, start):
        visited = [False] * self.V
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if visited[neighbor] == False: # '==' instead of 'is False'
                    queue.append(neighbor)
                    visited[neighbor] = True

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS Traversal starting from node 2:")
g.DFS(2)

print("\nBFS Traversal starting from node 2:")
g.BFS(2)
