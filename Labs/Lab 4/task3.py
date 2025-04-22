import heapq

delivery_points = {
    'A': {'coords': (0, 0), 'time_window': (0, 10)},
    'B': {'coords': (2, 4), 'time_window': (5, 15)},
    'C': {'coords': (5, 3), 'time_window': (8, 18)},
    'D': {'coords': (7, 8), 'time_window': (12, 20)},
}

def calculate_distance(point1, point2):
    # Calculate Euclidean distance between two points (x1, y1) and (x2, y2)
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

def greedy_best_first_search(delivery_points, start):
    open_list = []
    heapq.heappush(open_list, (0, 0, start, [start]))  # (heuristic, current_time, current_point, path)

    visited = set()

    while open_list:
        _, current_time, current_point, path = heapq.heappop(open_list)

        if len(path) == len(delivery_points):
            return path, current_time

        visited.add(current_point)
        for neighbor, details in delivery_points.items():
            if neighbor not in visited:
                coords = details['coords']
                time_window = details['time_window']
                start_time, end_time = time_window
                
                distance = calculate_distance(delivery_points[current_point]['coords'], coords)

                new_time = current_time + distance

                if new_time >= start_time and new_time <= end_time:
                    # Heuristic: prioritize the nearest point with respect to time window urgency
                    time_penalty = max(0, start_time - new_time)  # Penalty if we're early
                    heuristic_cost = distance + time_penalty

                    heapq.heappush(open_list, (heuristic_cost, new_time, neighbor, path + [neighbor]))

    return None, float('inf')  

start_point = 'A'

# Run the Greedy Best-First Search to find the optimal route
optimal_path, total_time = greedy_best_first_search(delivery_points, start_point)

print("Optimal Delivery Route:", optimal_path)
print("Total Time Taken:", total_time)
