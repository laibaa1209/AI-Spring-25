class Environment:
    def __init__(self, graph):
        self.graph = graph
    
    def get_neighbours(self, node):
        return self.graph.get(node, [])
    
class Agent:
    def __init__(self, goal):
        self.goal = goal
    
    def dfs_search(self, start, env):

        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(f"Visiting {node}")

            if node == self.goal:
                return f"Goal {self.goal} found!"
            for neighbours in reversed(env.get_neighbours(node)):
                if neighbours not in visited:
                    visited.append(neighbours)
                    stack.append(neighbours)
            
        return "Goal not found!"
    
    def act(self, start, env):
        print(f"Finding goal {self.goal} from the position {start}")
        goal_status = self.dfs_search(start, env)

        if goal_status == "Goal not found!":
            print("The goal state does not exist or was not found")
        else:
            print(f"Goal {self.goal} found!")
            
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H']
    }
    env = Environment(graph)
    agent = Agent('H')

    agent.act('A', env)

main()