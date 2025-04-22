from collections import deque

class BiGraph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start, visited, parent):
        q = deque([start])
        visited[start] = True

        while q:
            node = q.popleft()
            for neighbor in self.adj.get(node, []):
                if not visited.get(neighbor):
                    visited[neighbor] = True
                    parent[neighbor] = node
                    q.append(neighbor)

    def bidirectional_search(self, src, goal):
        if src == goal:
            return [src]

        visited_src = {}
        visited_goal = {}
        parent_src = {src: None}
        parent_goal = {goal: None}

        frontier_src = deque([src])
        frontier_goal = deque([goal])
        visited_src[src] = True
        visited_goal[goal] = True

        while frontier_src and frontier_goal:
            self.bfs_level(frontier_src, visited_src, parent_src)
            self.bfs_level(frontier_goal, visited_goal, parent_goal)

            intersection = set(visited_src.keys()) & set(visited_goal.keys())
            if intersection:
                meet = intersection.pop()
                path = self.reconstruct_path(meet, parent_src, parent_goal)
                return path

        return None

    def bfs_level(self, frontier, visited, parent):
        for _ in range(len(frontier)):
            node = frontier.popleft()
            for neighbor in self.adj.get(node, []):
                if not visited.get(neighbor):
                    visited[neighbor] = True
                    parent[neighbor] = node
                    frontier.append(neighbor)

    def reconstruct_path(self, meet, parent_src, parent_goal):
        path = []
        node = meet
        while node is not None:
            path.append(node)
            node = parent_src[node]
        path = path[::-1]
        node = parent_goal[meet]
        while node is not None:
            path.append(node)
            node = parent_goal[node]
        return path

# Example usage
bg = BiGraph()
bg.add_edge('A', 'B')
bg.add_edge('B', 'C')
bg.add_edge('C', 'D')
bg.add_edge('D', 'E')
bg.add_edge('E', 'F')

print("Bidirectional Search Path:", bg.bidirectional_search('A', 'F'))
