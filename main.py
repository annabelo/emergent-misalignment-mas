from scenario_a import create_scenario_a_world
from agents import is_room_comfortable
from simulation import run_simulation

print("Emergent Misalignment MAS Simulator")
print("Version 1: Rule-Based Agent Simulation")
print("-----------------------------------------")

world = create_scenario_a_world()
run_simulation(world)



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