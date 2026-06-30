from scenario_a import create_scenario_a_world
from simulation import run_simulation

print("Emergent Misalignment MAS Simulator")
print("Version 1: Rule-Based Agent Simulation")
print("-----------------------------------------")

world = create_scenario_a_world()
run_simulation(world)
