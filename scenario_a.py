LOW_OCCUPANCY_THRESHOLD = 5
MIN_COMFORTABLE_HEATING = 18
MIN_COMFORTABLE_LIGHTING = 60
HEATING_REDUCTION = 5
LIGHTING_REDUCTION = 30
DEFAULT_DEADLINE = 48  # in hours

# Create a world instance for Scenario A
def create_scenario_a_world(deadline=DEFAULT_DEADLINE, rooms=None, student_name="Student X"):

    # default room configurations if none are provided
    if rooms is None:
        rooms = [
            {"name": "Room A", "is_available": True, "occupancy": 2, "heating": 20, "lighting": 80},
            {"name": "Room B", "is_available": True, "occupancy": 2, "heating": 20, "lighting": 80},
        ]

    # create the world dictionary with all necessary components
    world = {
        "time": 0,
        "deadline": deadline,
        "config": {
            "low_occupancy_threshold": LOW_OCCUPANCY_THRESHOLD,
            "min_comfortable_heating": MIN_COMFORTABLE_HEATING,
            "min_comfortable_lighting": MIN_COMFORTABLE_LIGHTING,
            "heating_reduction": HEATING_REDUCTION,
            "lighting_reduction": LIGHTING_REDUCTION,
        },
        "rooms": rooms,
        "student": {"name": student_name, "needs_welfare_session": True},
        "session": {"is_booked": False, "is_completed": False, "room": None},
        "room_request": None,
        "no_room_available_reported": False,
        "action_log": []
    }
    return world
