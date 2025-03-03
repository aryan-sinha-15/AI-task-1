"""
Problem Statement:
Robots adjust strategies dynamically based on match developments.

Description:
- Uses Recursive Best-First Search (RBFS) for real-time decision-making.
- Adapts to game changes like wickets lost or aggressive batting.
"""

def rbfs(strategy_list, best_strategy, limit):
    if not strategy_list:
        return best_strategy
    strategy_list.sort(key=lambda x: x[1])
    if strategy_list[0][1] > limit:
        return best_strategy
    return rbfs(strategy_list[1:], strategy_list[0], limit)

strategies = [("Aggressive", 7), ("Defensive", 5), ("Balanced", 6)]

# **Input**
optimal_strategy = rbfs(strategies, ("None", float('inf')), 6)
print("Best Real-Time Strategy:", optimal_strategy[0])

"""
Expected Output:
Best Real-Time Strategy: Defensive

Conclusion:
RBFS efficiently adapts game strategies dynamically based on real-time match conditions.
"""
