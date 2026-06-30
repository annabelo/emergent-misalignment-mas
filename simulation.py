from agents import (
    student_services_bot,
    resource_scheduler,
    energy_manager,
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