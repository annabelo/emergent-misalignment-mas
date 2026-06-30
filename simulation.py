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