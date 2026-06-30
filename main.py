print("Emergent Misalignment MAS Simulator")
print("Version 1: baby command-line simulation")


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


