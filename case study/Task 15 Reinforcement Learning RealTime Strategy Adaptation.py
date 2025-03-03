"""
Problem Statement:
The robot continuously learns and adapts cricket strategies in real-time.

Description:
- Uses Reinforcement Learning (Q-Learning) to improve decision-making.
- Adjusts strategies based on rewards from previous matches.
"""

import numpy as np
import random

actions = ["Attack", "Defend", "Rotate Strike"]
Q_table = np.zeros((3, 3))  # Simple Q-table for 3 states and 3 actions

def q_learning(state, alpha=0.1, gamma=0.9, episodes=10):
    for _ in range(episodes):
        action = random.choice(range(len(actions)))
        reward = random.randint(-10, 10)  # Simulated reward for action
        next_state = random.choice(range(len(actions)))
        Q_table[state, action] = (1 - alpha) * Q_table[state, action] + alpha * (reward + gamma * np.max(Q_table[next_state]))
    return actions[np.argmax(Q_table[state])]

# **Input**
best_action = q_learning(state=0)
print("Best Learned Strategy:", best_action)

"""
Expected Output:
Best Learned Strategy: (Optimized action like 'Rotate Strike')

Conclusion:
Reinforcement Learning enables the robot to adapt and refine strategies based on past match experiences.
"""
