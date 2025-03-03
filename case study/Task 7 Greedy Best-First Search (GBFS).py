"""
Problem Statement:
The robot monitors players with the highest impact on the match’s outcome.

Description:
- Uses Greedy Best First Search (GBFS) to track high-impact players.
- Prioritizes players based on recent performance metrics like runs, wickets, and fielding impact.
"""

import heapq

class Player:
    def __init__(self, name, impact_score):
        self.name = name
        self.impact_score = impact_score

    def __lt__(self, other):
        return self.impact_score > other.impact_score  # Higher impact players are prioritized

# Player list with impact scores
players = [
    Player("Player A", 85),
    Player("Player B", 92),
    Player("Player C", 76),
    Player("Player D", 88),
]

# Using Greedy Best First Search to select top player
priority_queue = []
for player in players:
    heapq.heappush(priority_queue, player)

# **Input**
top_performer = heapq.heappop(priority_queue)
print("Top Performing Player:", top_performer.name)

"""
Expected Output:
Top Performing Player: Player B

Conclusion:
GBFS efficiently prioritizes tracking the most impactful players using a heuristic (impact score).
"""
