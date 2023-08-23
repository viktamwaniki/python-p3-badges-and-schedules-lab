def badge_maker(name):
    message = "Hello, my name is " + name + "."
    return message

def batch_badge_creator(speaker_names):
    badge_messages = [badge_maker(name) for name in speaker_names]
    return badge_messages

def assign_rooms(speaker_names):
    room_assignments = []
    rooms = range(1, 8)  # Rooms 1 to 7
    
    for i, name in enumerate(speaker_names):
        room_assignment = "Hello, " + name + "! You'll be assigned to room " + str(rooms[i]) + "!"
        room_assignments.append(room_assignment)
        
    return room_assignments

def printer(speaker_names):
    badge_messages = batch_badge_creator(speaker_names)
    room_assignments = assign_rooms(speaker_names)
    
    for badge_message in badge_messages:
        print(badge_message)
    
    for room_assignment in room_assignments:
        print(room_assignment)
