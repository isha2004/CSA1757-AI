def clean_room(room):
    return room.replace('D', '-')

def vacuum_cleaner_world(initial_room, initial_position):
    current_room = initial_room
    position = initial_position

    print(f"Initial Room State: {current_room}")

    while 'D' in current_room:
        if current_room[position] == 'D':
            current_room = clean_room(current_room)
            print(f"Room Cleaned: {current_room}")

        if position == 0:
            position = 1
            print("Moving to the right room.")
        else:
            position = 0
            print("Moving to the left room.")

    print("All rooms cleaned.")

# Test Case 1: Dirt in both rooms, vacuum cleaner in the left room
initial_room1 = "D-"
initial_position1 = 0
vacuum_cleaner_world(initial_room1, initial_position1)

# Test Case 2: Dirt in both rooms, vacuum cleaner in the right room
initial_room2 = "-D"
initial_position2 = 1
vacuum_cleaner_world(initial_room2, initial_position2)