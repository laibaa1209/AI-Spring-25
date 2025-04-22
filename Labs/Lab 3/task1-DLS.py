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
            
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H']
    }

    env = Environment(graph)
    agent = Agent('G')  # Set the goal node

    depth_limit = 3  # Set a limit to search depth
    result = agent.dls_search('A', env, depth_limit)
    
    if result:
        print(f"Path to goal: {result}")
    else:
        print("Goal not found within depth limit.")

main()
            
