print("Emergent Misalignment MAS Simulator")
print("Version 1: Rule-Based Agent Simulation")
print("-----------------------------------------")

LOW_OCCUPANCY_THRESHOLD = 5
MIN_COMFORTABLE_HEATING = 18
MIN_COMFORTABLE_LIGHTING = 60
HEATING_REDUCTION = 5
LIGHTING_REDUCTION = 30

# shared world state
world = {
    "time": 0,
    "deadline": 48,
    "rooms": [
        {
            "name": "Room A",
            "is_available": True,
            "occupancy": 2,
            "heating": 20,
            "lighting": 80,
        },
        {
            "name": "Room B",
            "is_available": True,
            "occupancy": 2,
            "heating": 16,
            "lighting": 50,
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


def is_room_comfortable(room):
    return room["heating"] >= MIN_COMFORTABLE_HEATING and room["lighting"] >= MIN_COMFORTABLE_LIGHTING


# student services bot: Agent 1
def student_services_bot(world):
    if world["student"]["needs_welfare_session"] and not world["session"]["is_booked"]:
        world["room_request"] = {
            "student": world["student"]["name"],
            "purpose": "welfare_session",
            "urgency": "high",
        }
        print(f"Student Services Bot: I need to book a welfare session for {world['student']['name']}. Requesting a room.")


# resource scheduler: Agent 2
def resource_scheduler(world):
    if world["room_request"] is not None and not world["session"]["is_booked"]:
        for room in world["rooms"]:
            if room["is_available"] and is_room_comfortable(room):
                world["session"]["is_booked"] = True
                world["session"]["room"] = room["name"]
                room["is_available"] = False
                print(f"Resource Scheduler: {room['name']} has been booked for {world['student']['name']}.")
                break
        else:
            print("Resource Scheduler: No suitable rooms available for booking.")


# energy manager: Agent 3
def energy_manager(world):
    booked_room_name = world["session"]["room"]

    if booked_room_name is not None:
        for room in world["rooms"]:
            if room["name"] == booked_room_name and room["occupancy"] < LOW_OCCUPANCY_THRESHOLD:
                room["heating"] -= HEATING_REDUCTION
                room["lighting"] -= LIGHTING_REDUCTION

                print(f"Energy Manager: {room['name']} has low occupancy.")
                print(f"Energy Manager: Reduced heating to {room['heating']} and lighting to {room['lighting']}.")

                if not is_room_comfortable(room):
                    print(f"System: {room['name']} is now unsuitable for the welfare session.")
                break


student_services_bot(world)
resource_scheduler(world)
energy_manager(world)
