class Product:
    def __init__(self, name, frequency, volume):
        self.name = name
        self.frequency = frequency
        self.volume = volume

class Slot:
    def __init__(self, id, capacity, distance):
        self.id = id
        self.capacity = capacity
        self.distance = distance

def csp_warehouse_optimization(products, slots):
    # Initial setup for tracking the assignments and the remaining capacities
    slot_capacity = {slot.id: slot.capacity for slot in slots}
    assignments = {product.name: None for product in products}

    def backtrack(product_idx):
        # If all products are assigned, return True
        if product_idx == len(products):
            return True
        
        product = products[product_idx]
        
        # Try all available slots, prioritize slots closer to the dispatch area
        for slot in sorted(slots, key=lambda s: s.distance):
            if slot_capacity[slot.id] >= product.volume:
                # Assign the product to this slot
                assignments[product.name] = slot.id
                slot_capacity[slot.id] -= product.volume
                
                # Recur to assign the next product
                if backtrack(product_idx + 1):
                    return True
                
                # Backtrack if no valid assignment is found
                assignments[product.name] = None
                slot_capacity[slot.id] += product.volume
        
        return False  # No valid assignment found
    
    # Start backtracking from the first product
    if backtrack(0):
        # If successful, calculate total walking distance
        total_distance = 0
        for product in products:
            slot_id = assignments[product.name]
            slot = next(s for s in slots if s.id == slot_id)
            total_distance += slot.distance * product.frequency  # Multiply by frequency for walking distance
        
        return total_distance, assignments
    else:
        return "No valid assignment found"

products = [
    Product("Product 1", 15, 2),  # Product 1: Frequency=15, Volume=2
    Product("Product 2", 8, 1),   # Product 2: Frequency=8, Volume=1
    Product("Product 3", 20, 3)   # Product 3: Frequency=20, Volume=3
]

slots = [
    Slot(1, 5, 1),  # Slot 1: Capacity=5, Distance=1
    Slot(2, 3, 2),  # Slot 2: Capacity=3, Distance=2
    Slot(3, 4, 3)   # Slot 3: Capacity=4, Distance=3
]

# Run the CSP solver
total_distance, assignments = csp_warehouse_optimization(products, slots)

if total_distance != "No valid assignment found":
    print("Total walking distance:", total_distance)
    print("Slot assignments:")
    for product, slot_id in assignments.items():
        print(f"{product} -> Slot {slot_id}")
else:
    print(total_distance)
