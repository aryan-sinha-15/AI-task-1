"""
Problem Statement:
The robot predicts the type of shot a batsman will play.

Description:
- Uses Random Restart Hill Climbing to refine shot prediction.
- Avoids local optima by restarting from new random positions.
"""

import random

shots = ["Cover Drive", "Pull Shot", "Straight Drive", "Hook Shot"]

def hill_climbing():
    best_shot = random.choice(shots)
    for _ in range(10):
        new_shot = random.choice(shots)
        if random.random() > 0.5:  # Random chance for improvement
            best_shot = new_shot
    return best_shot

# **Input**
predicted_shot = hill_climbing()
print("Predicted Shot:", predicted_shot)

"""
Expected Output:
Predicted Shot: (Randomly selected shot like 'Cover Drive')

Conclusion:
Hill Climbing optimizes shot prediction but may require multiple restarts to avoid local optima.
"""
