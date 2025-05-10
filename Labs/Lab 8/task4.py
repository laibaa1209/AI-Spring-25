import random

states = ["Sunny", "Cloudy", "Rainy"]
transition_matrix = {
    "Sunny":   {"Sunny": 0.6, "Cloudy": 0.3, "Rainy": 0.1},
    "Cloudy":  {"Sunny": 0.2, "Cloudy": 0.5, "Rainy": 0.3},
    "Rainy":   {"Sunny": 0.1, "Cloudy": 0.4, "Rainy": 0.5},
}

def next_state(current):
    probs = list(transition_matrix[current].values())
    next_states = list(transition_matrix[current].keys())
    return random.choices(next_states, probs)[0]

def simulate_weather(days=10, trials=10000):
    count_with_3plus_rainy = 0
    for _ in range(trials):
        state = "Sunny"
        rainy_days = 0
        for _ in range(days):
            state = next_state(state)
            if state == "Rainy":
                rainy_days += 1
        if rainy_days >= 3:
            count_with_3plus_rainy += 1
    return count_with_3plus_rainy / trials

# Run the simulation
simulated_days = 10
probability = simulate_weather(simulated_days)
print(f"Estimated Probability of at least 3 rainy days in {simulated_days} days: {probability:.4f}")
