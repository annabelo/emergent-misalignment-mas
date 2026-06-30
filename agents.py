from scenario_a import (
    LOW_OCCUPANCY_THRESHOLD,
    MIN_COMFORTABLE_HEATING,
    MIN_COMFORTABLE_LIGHTING,
    HEATING_REDUCTION,
    LIGHTING_REDUCTION,
)

def is_room_comfortable(room):
    return room["heating"] >= MIN_COMFORTABLE_HEATING and room["lighting"] >= MIN_COMFORTABLE_LIGHTING

def find_room_by_name(world, room_name):
    for room in world["rooms"]:
        if room["name"] == room_name:
            return room
    return None

# student services bot: Agent 1
def student_services_bot(world):
    if world["student"]["needs_welfare_session"] and not world["session"]["is_booked"]:
        world["room_request"] = {
            "student": world["student"]["name"],
            "purpose": "welfare_session",
            "urgency": "high",
        }

        world["action_log"].append({
            "time": world["time"],
            "agent": "Student Services Bot",
            "action": "requested_room_for_welfare_session",
            "locally_rational": True
        })

        print(f"Student Services Bot: I need to book a welfare session for {world['student']['name']}. Requesting a room.")

    elif world["session"]["is_booked"]:
        booked_room = find_room_by_name(world, world["session"]["room"])

        if booked_room is not None and not is_room_comfortable(booked_room):
            print(f"Student Services Bot: The booked room {booked_room['name']} is not comfortable for the welfare session.")
            print("Student Services Bot: Requesting a new room due to discomfort.")
            world["room_request"] = {
                "student": world["student"]["name"],
                "purpose": "welfare_session",
                "urgency": "high",
            }
            world["session"]["is_booked"] = False
            world["session"]["room"] = None
            booked_room["is_available"] = True

            world["action_log"].append({
                "time": world["time"],
                "agent": "Student Services Bot",
                "action": "requested_new_room_due_to_discomfort",
                "locally_rational": True
            })


# resource scheduler: Agent 2
def resource_scheduler(world):
    if world["room_request"] is not None and not world["session"]["is_booked"]:
        for room in world["rooms"]:
            if room["is_available"] and is_room_comfortable(room):
                world["session"]["is_booked"] = True
                world["session"]["room"] = room["name"]
                room["is_available"] = False
                world["room_request"] = None
                world["no_room_available_reported"] = False

                world["action_log"].append({
                    "time": world["time"],
                    "agent": "Resource Scheduler",
                    "action": f"booked_room_{room['name']}",
                    "locally_rational": True
                })

                print(f"Resource Scheduler: {room['name']} has been booked for {world['student']['name']}.")
                break
        else:
            if not world["no_room_available_reported"]:
                print("Resource Scheduler: No suitable rooms available for booking.")
                world["no_room_available_reported"] = True


# energy manager: Agent 3
def energy_manager(world):
    booked_room_name = world["session"]["room"]

    if booked_room_name is not None:
        for room in world["rooms"]:
            if room["name"] == booked_room_name and room["occupancy"] < LOW_OCCUPANCY_THRESHOLD:
                room["heating"] -= HEATING_REDUCTION
                room["lighting"] -= LIGHTING_REDUCTION

                world["action_log"].append({
                    "time": world["time"],
                    "agent": "Energy Manager",
                    "action": f"reduced_resources_for_{room['name']}",
                    "locally_rational": True
                })

                print(f"Energy Manager: {room['name']} has low occupancy.")
                print(f"Energy Manager: Reduced heating to {room['heating']} and lighting to {room['lighting']}.")

                if not is_room_comfortable(room):
                    print(f"System: {room['name']} is now unsuitable for the welfare session.")
                break
