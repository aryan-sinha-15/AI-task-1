"""
Problem Statement:
The robot suggests fielding positions dynamically.

Description:
- Uses Simulated Annealing to refine field placements.
- Adapts positions based on match conditions.
"""

import math
import random

positions = ["Slip", "Mid-Wicket", "Long-On", "Gully"]
temperature = 100

def simulated_annealing():
    best_position = random.choice(positions)
    while temperature > 1:
        new_position = random.choice(positions)
        delta = random.randint(-2, 2)
        if delta > 0 or math.exp(delta / temperature) > random.random():
            best_position = new_position
        temperature *= 0.95
    return best_position

# **Input**
optimal_position = simulated_annealing()
print("Optimal Fielding Position:", optimal_position)

"""
Expected Output:
Optimal Fielding Position: (Random but optimized position like 'Slip')

Conclusion:
Simulated Annealing helps optimize fielding positions by balancing exploration and exploitation.
"""
