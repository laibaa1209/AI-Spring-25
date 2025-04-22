import heapq
import random
import time

# Example graph with initial edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# Heuristic function (straight-line distance to goal)
def heuristic(node, goal):
    heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    return heuristics[node]

def astar_search(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, None))  # (f, g, node, parent)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        # Pop the node with the lowest f_score
        _, current_g, current, parent = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct the path
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return current_g, list(reversed(path))

        # Check the neighbors
        for neighbor, weight in graph.get(current, []):
            # Dynamically adjust the edge cost randomly (simulate change)
            weight = random.choice([weight, weight + random.randint(-1, 3)])  # Randomly modify edge cost

            tentative_g_score = current_g + weight
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor, current))

        time.sleep(1)  # Sleep for a second to simulate dynamic changes in edge costs

    return float('inf'), []

# Example usage
start_node = 'A'
goal_node = 'D'

cost, path = astar_search(graph, start_node, goal_node)
print("Optimal Path:", path)
print("Total Cost:", cost)
