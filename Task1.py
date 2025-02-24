# Define the table with cleaning actions
cleaning_table = {
    'A': {'dirty': 'clean', 'clean': 'move to B'},
    'B': {'dirty': 'clean', 'clean': 'move to C'},
    'C': {'dirty': 'clean', 'clean': 'move to D'},
    'D': {'dirty': 'clean', 'clean': 'done'}
}

# Rooms with initial dirt status
rooms = {'A': 'dirty', 'B': 'dirty', 'C': 'dirty', 'D': 'dirty'}

# Function to clean the rooms based on the table-driven approach
def table_driven_cleaning():
    for room in ['A', 'B', 'C', 'D']:
        action = cleaning_table[room][rooms[room]]
        print(f"Room {room} is {rooms[room]}. Action: {action}")
        
        if action == 'clean':
            rooms[room] = 'clean'  # Update status after cleaning
        elif action == 'done':
            print("All rooms are clean!")
            break

table_driven_cleaning()
