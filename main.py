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
    }
}

# student services bot: Agent 1
def student_services_bot(world):
    if world["student"]["needs_welfare_session"] and not world["session"]["is_booked"]:
        print("Student Services Bot: I need to book a welfare session for the student.")




student_services_bot(world)


