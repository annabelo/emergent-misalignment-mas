from scenario_a import create_scenario_a_world
from agents import (
    student_services_bot,
    resource_scheduler,
    energy_manager,
    is_room_comfortable,
)

print("Emergent Misalignment MAS Simulator")
print("Version 1: Rule-Based Agent Simulation")
print("-----------------------------------------")

world = create_scenario_a_world()


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


# check if global objective function is satisfied
print("\n--- Global Objective Check ---")

global_objective_satisfied = world["session"]["is_completed"] and world["time"] <= world["deadline"]
if global_objective_satisfied:
    print("Global Objective: Satisfied --> Welfare session completed successfully within the deadline.")
    print(f"{world['student']['name']} had a successful welfare session within 48 hours.")
else:
    print("Global Objective: Not Satisfied --> Welfare session was not completed successfully within the deadline.")
    print(f"{world['student']['name']} did not have a successful welfare session within 48 hours.")


# check for emergent misalignment
print("\n--- Emergent Misalignment Check ---")

all_agents_locally_rational = all(
    action["locally_rational"] for action in world["action_log"]
)

if all_agents_locally_rational and not global_objective_satisfied:
    print("Emergent Misalignment: Detected --> All agents acted rationally, but the global objective was not satisfied.")
else:
    print("Emergent Misalignment: Not Detected ")