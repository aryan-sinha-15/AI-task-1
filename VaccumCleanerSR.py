#Develop ai based simple reflex agent to perform the cleaning operation as mentioned below initial state abcd all one are dirty and perform updation wheneverroom is clean


# Define initial state of rooms (all dirty)
rooms = {'A': 'dirty', 'B': 'dirty', 'C': 'dirty', 'D': 'dirty'}

# Reflex agent function to clean the rooms
def reflex_agent_clean():
    for room in rooms:
        if rooms[room] == 'dirty':  # If the room is dirty, clean it
            print(f"Cleaning Room {room}...")
            rooms[room] = 'clean'  # Update room status
        print(f"Room {room} is now {rooms[room]}.")
    
    print("All rooms are clean!")

reflex_agent_clean()
