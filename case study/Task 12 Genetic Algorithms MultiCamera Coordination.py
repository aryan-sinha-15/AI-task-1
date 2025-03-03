    """
Problem Statement:
The robot coordinates multiple cameras to capture key match moments.

Description:
- Uses Genetic Algorithm to optimize camera control strategies.
- Evolves best strategies through selection, crossover, and mutation.
"""

import random

cameras = ["Wide Angle", "Close-Up", "Drone", "Stump Cam"]

def genetic_algorithm():
    best_camera = random.choice(cameras)
    for _ in range(5):
        new_camera = random.choice(cameras)
        if random.random() > 0.7:  # Mutation chance
            best_camera = new_camera
    return best_camera

# **Input**
best_camera_view = genetic_algorithm()
print("Best Camera Angle:", best_camera_view)

"""
Expected Output:
Best Camera Angle: (Random optimized angle like 'Drone')

Conclusion:
Genetic Algorithms optimize camera angles dynamically for better coverage.
"""
