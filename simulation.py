from agents import (
    student_services_bot,
    resource_scheduler,
    energy_manager,
    is_room_comfortable,
)

def run_simulation(world):
    for timestep in range(1, world["deadline"] + 1):
        print(f"\n--- Hour {timestep} ---")
        world["time"] = timestep

        student_services_bot(world)
        resource_scheduler(world)
        energy_manager(world)
        
    # print the action log
    print("\n--- Action Log ---")
    print(f"{'Hour':<6} | {'Agent':<25} | {'Action':<50} | {'Locally Rational'}")
    print("-" * 100)
    for action in world["action_log"]:
    
        print(
            f"{action['time']:<6} | "
            f"{action['agent']:<25} | "
            f"{action['action']:<50} | "
            f"{action['locally_rational']}"
        )
    
    print("\n--- Final Room States ---")
    print(f"{'Room':<10} | {'Available':<10} | {'Occupancy':<10} | {'Heating':<10} | {'Lighting':<10} | {'Comfortable'}")
    print("-" * 90)

    for room in world["rooms"]:
        print(
            f"{room['name']:<10} | "
            f"{str(room['is_available']):<10} | "
            f"{room['occupancy']:<10} | "
            f"{room['heating']:<10} | "
            f"{room['lighting']:<10} | "
            f"{is_room_comfortable(room)}"
        )
    