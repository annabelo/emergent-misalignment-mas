print("Emergent Misalignment MAS Simulator")
print("Version 1: Rule-Based Agent Simulation")

# shared world state
world = {
    "time": 0,
    "deadline": 48,
    "rooms": [
        {
            "name": "Room A",
            "is_available": True,
            "is_comfortable": True,
        },
        {
            "name": "Room B",
            "is_available": True,
            "is_comfortable": False,
        }
    ],
    "student": {
        "name": "Student X",
        "needs_welfare_session": True,
    },
    "session": {
        "is_booked": False,
        "is_completed": False,
        "room": None,
    },
    "room_request": None
}

# student services bot: Agent 1
def student_services_bot(world):
    if world["student"]["needs_welfare_session"] and not world["session"]["is_booked"]:
        world["room_request"] = {
            "student": world["student"]["name"],
            "purpose": "welfare_session",
            "urgency": "high",
        }
        print(f"Student Services Bot: I need to book a welfare session for {world['student']['name']} requesting a room.")

# resource scheduler: Agent 2
def resource_scheduler(world):
    if world["room_request"] is not None and not world["session"]["is_booked"]:
        for room in world["rooms"]:
            if room["is_available"] and room["is_comfortable"]:
                world["session"]["is_booked"] = True
                world["session"]["room"] = room["name"]
                room["is_available"] = False
                print(f"Resource Scheduler: {room['name']} has been booked for {world['student']['name']}.")
                break
        else:
            print("Resource Scheduler: No suitable rooms available for booking.")


student_services_bot(world)
resource_scheduler(world)



