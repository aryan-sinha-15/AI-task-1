#Monkey Banana problemcompetitive monkey banana problem


import time
import random

# Define monkeys' positions
monkey1 = "Room"
monkey2 = "Room"
ladder = "Other Room"
banana = "Room"

# Function to simulate the competition
def monkey_race():
    print("🏁 Race Started! Monkeys running to the ladder...")

    # Random time taken by each monkey to reach the ladder
    t1 = random.uniform(1, 3)  
    t2 = random.uniform(1, 3)  
    
    time.sleep(min(t1, t2))  # Simulate movement delay
    
    winner = "Monkey 1" if t1 < t2 else "Monkey 2"
    print(f"🥇 {winner} reached the ladder first!")

    print(f"{winner} is bringing the banana back...")
    time.sleep(2)  # Simulate return time
    print(f"🎉 {winner} wins by bringing the banana!")

monkey_race()
