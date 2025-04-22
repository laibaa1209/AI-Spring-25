class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    def dls(self, src, goal, limit, visited):
        if src == goal:
            return [src]
        if limit <= 0:
            return None
        visited.add(src)

        for neighbor in self.adj.get(src, []):
            if neighbor not in visited:
                path = self.dls(neighbor, goal, limit - 1, visited)
                if path:
                    return [src] + path
        return None

    def iddfs(self, src, goal, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            path = self.dls(src, goal, depth, visited)
            if path:
                return path
        return None

# Example tree-like graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

print("IDDFS Path:", g.iddfs('A', 'F', 5))
