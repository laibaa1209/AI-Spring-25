import heapq

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbours(self, node):
        return self.graph.get(node, [])

class UtilityBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def ucs(self, start, env):
        frontier = []
        heapq.heappush(frontier, (0, start, []))  # (cost, node, path)
        explored = set()

        while frontier:
            cost, current_node, path = heapq.heappop(frontier)
            path = path + [current_node]

            print(f"Exploring: {current_node}, Cost so far: {cost}")

            if current_node == self.goal:
                return f"Goal '{self.goal}' reached with total cost {cost}. Path: {path}"

            if current_node not in explored:
                explored.add(current_node)

                for neighbour, step_cost in env.get_neighbours(current_node):
                    if neighbour not in explored:
                        heapq.heappush(frontier, (cost + step_cost, neighbour, path))

        return f"Goal '{self.goal}' not reachable from '{start}'."

    def act(self, start, env):
        print(f"Agent starting UCS from '{start}' to reach goal '{self.goal}'.")
        result = self.ucs(start, env)
        print(f"Action Result: {result}")


def main():
    graph = {
        'A': [('B', 1), ('C', 5)],
        'B': [('D', 3), ('E', 1)],
        'C': [('F', 2), ('G', 8)],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    env = Environment(graph)
    agent = UtilityBasedAgent(goal='F')

    agent.act(start='A', env=env)

main()
