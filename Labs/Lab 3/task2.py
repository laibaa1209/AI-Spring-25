#UCS implementation of travleeing salesman problem.
import heapq

# Distance matrix
dist = {
    1: {2: 10, 3: 15, 4: 20},
    2: {1: 10, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 20, 2: 25, 3: 30}
}

class TSPAgent:
    def __init__(self, graph):
        self.graph = graph

    def uniform_cost_search(self, start):
        frontier = []
        heapq.heappush(frontier, (0, [start]))  # (cost, path)

        best_path = None
        min_cost = float('inf')

        while frontier:
            cost, path = heapq.heappop(frontier)
            current = path[-1]

            if len(path) == len(self.graph) and start in self.graph[current]:
                total_cost = cost + self.graph[current][start]  # Return to start
                path_complete = path + [start]

                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path_complete

            for neighbor, edge_cost in self.graph[current].items():
                if neighbor not in path:
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (cost + edge_cost, new_path))

        return best_path, min_cost

agent = TSPAgent(dist)
best_path, min_cost = agent.uniform_cost_search(1)

print("Best path:", best_path)
print("Minimum cost:", min_cost)
