LOW_OCCUPANCY_THRESHOLD = 5
MIN_COMFORTABLE_HEATING = 18
MIN_COMFORTABLE_LIGHTING = 60
HEATING_REDUCTION = 5
LIGHTING_REDUCTION = 30


def create_scenario_a_world(deadline=48, rooms=None):
    if rooms is None:
        rooms = [
            {"name": "Room A", "is_available": True, "occupancy": 2, "heating": 20, "lighting": 80},
            {"name": "Room B", "is_available": True, "occupancy": 2, "heating": 20, "lighting": 80},
        ]

    world = {
        "time": 0,
        "deadline": deadline,
        "rooms": rooms,
        "student": {"name": "Student X", "needs_welfare_session": True},
        "session": {"is_booked": False, "is_completed": False, "room": None},
        "room_request": None,
        "no_room_available_reported": False,
        "action_log": []
    }
    return world
