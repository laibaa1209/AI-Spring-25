class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbours(self, node):
        return self.graph.get(node, [])

class Agent:
    def __init__(self, goal):
        self.goal = goal

    def dls_search(self, start, env, depth_limit):
        visited = []

        def dfs(node, depth, path):
            if depth > depth_limit:
                return None
            
            visited.append(node)
            path.append(node)
            print(f"Visiting: {node}, Depth: {depth}")

            if node == self.goal:
                return f"Goal {self.goal} found at depth {depth}.\nThe path was {path}"
            
            for neighbour in env.get_neighbours(node):
                if neighbour not in visited:
                    result = dfs(neighbour, depth + 1, path)
                    if result:
                        return result
            visited.pop()
            path.pop()
            return None
        
        return dfs(start, 0, [])

    def act(self, start, env, depth_limit):
        print(f"Agent starting search for goal '{self.goal}' from node '{start}' with depth limit {depth_limit}.")
        result = self.dls_search(start, env, depth_limit)
        if result:
            print(f"Action Result: {result}")
        else:
            print(f"Goal '{self.goal}' not found within depth limit {depth_limit}.")

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H']
    }

    env = Environment(graph)
    agent = Agent('G') 

    depth_limit = 3  
    agent.act('A', env, depth_limit)  

main()
