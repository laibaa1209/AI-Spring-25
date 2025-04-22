from queue import PriorityQueue

graph = {
    'A': [('B', 5), ('C', 8)],
    'B': [('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 7)],
    'E': [('F', 2)],
    'F': []
}

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))  # (priority, path)

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]
        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    pq.put((weight, path + [neighbor]))

    return float('inf'), []

def multi_goal_best_path(graph, start, goals):
    best_cost = 0
    best_path = [start]
    current = start
    remaining_goals = set(goals)

    while remaining_goals:
        # Find the closest goal to the current node using Best-First Search
        closest_goal = None
        min_cost = float('inf')
        path_to_closest_goal = []

        for goal in remaining_goals:
            cost, path = best_first_search(graph, current, goal)
            if cost < min_cost:
                min_cost = cost
                closest_goal = goal
                path_to_closest_goal = path

        if closest_goal is None:
            break  # No more reachable goals

        # Update best cost and path
        best_cost += min_cost
        best_path.extend(path_to_closest_goal[1:])  # Skip the current node to avoid duplicates
        remaining_goals.remove(closest_goal)
        current = closest_goal

    return best_cost, best_path

# Example usage
start_node = 'A'
goal_nodes = {'D', 'E', 'F'}

cost, path = multi_goal_best_path(graph, start_node, goal_nodes)
print("Best-First Search Multi-Goal Path:", path)
print("Total Cost:", cost)
